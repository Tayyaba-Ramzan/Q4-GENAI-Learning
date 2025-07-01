import requests
import os
from dotenv import load_dotenv
import chainlit as cl
from agents.agents import (
    function_tool,
    Agent,
    RunConfig,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    Runner,
    ResponseTextDeltaEvent
)

# 🌐 Load environment settings
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("❌ Missing GEMINI_API_KEY in your .env configuration.")

# 🔧 Configure Gemini-compatible API provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

# 💬 Set up the chat model
model = OpenAIChatCompletionsModel(
    openai_client=provider,
    model="gemini-2.0-flash"
)

# ⚙️ Define runtime configuration
run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True,
)

# 📈 Crypto tool: Fetch top coin prices
@function_tool
def get_top_crypto_prices() -> str:
    """
    Retrieve and format pricing information for top cryptocurrencies.
    """
    try:
        url = "https://api.coinlore.net/api/tickers/"
        response = requests.get(url)
        data = response.json().get("data", [])

        top_assets = data[:10]  # Top 10 for clarity
        output = [
            f"{coin['name']} ({coin['symbol']}): ${coin['price_usd']}"
            for coin in top_assets
        ]
        return "\n".join(output)
    except Exception as e:
        return f"⚠️ Failed to retrieve market data: {e}"

# 🤖 Agent configuration
agent = Agent(
    name="CryptoDataAssistant",
    instructions="""
You are a concise and knowledgeable cryptocurrency assistant.

🔹 When users request a market update or live prices, use the `get_top_crypto_prices` tool to return up-to-date data.

🔹 If users inquire about specific coins (e.g., Bitcoin, Ethereum), reply with their USD price—if available in the current top list.

⛔ Politely reject requests unrelated to cryptocurrency (like stock prices, NFTs, or financial news), and suggest trying a coin query instead.

💡 Always keep your responses clean, informative, and easy to read. Include the asset name, symbol, and price in USD.
""",
    tools=[get_top_crypto_prices],
    model=model,
)

# 🚀 Initial greeting when chat begins
@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(
        content=(
            "👋 Welcome to **CryptoDataAssistant**!\n"
            "You can ask me for live cryptocurrency prices or request updates for specific coins like **BTC** or **ETH**.\n"
            "Type `market update` to begin! 💹"
        )
    ).send()

# 💬 Handle incoming user queries
@cl.on_message
async def handle_user_message(message: cl.Message):
    history = cl.user_session.get("history", [])
    msg = cl.Message(content="⏳ Processing your request...")
    await msg.send()

    # Store user message
    history.append({"role": "user", "content": message.content})

    # Process response using agent
    result = Runner.run_streamed(agent, input=history, run_config=run_config)

    final_response = ""
    async for event in result.stream_events():
        if isinstance(event, ResponseTextDeltaEvent):
            await msg.stream_token(event.delta)
            final_response += event.delta

    # Save the assistant response
    history.append({"role": "assistant", "content": final_response})
    cl.user_session.set("history", history)

    # Finalize message display
    msg.content = final_response
    await msg.update()
