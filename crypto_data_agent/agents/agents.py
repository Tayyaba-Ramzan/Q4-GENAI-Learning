from typing import Any, Callable, List
from dataclasses import dataclass

# ----------- Tool Decorator ----------- #
def function_tool(func: Callable) -> Callable:
    func._is_tool = True
    return func

# ----------- Gemini-Like Client Mock ----------- #
class AsyncOpenAI:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

# ----------- Model Config ----------- #
@dataclass
class OpenAIChatCompletionsModel:
    openai_client: AsyncOpenAI
    model: str

# ----------- Run Config ----------- #
@dataclass
class RunConfig:
    model: Any
    model_provider: Any
    tracing_disabled: bool = True

# ----------- Agent Structure ----------- #
@dataclass
class Agent:
    name: str
    instructions: str
    tools: List[Callable]
    model: Any

# ----------- Response Delta Event ----------- #
class ResponseTextDeltaEvent:
    def __init__(self, delta: str):
        self.delta = delta

# ----------- Runner Simulated Response ----------- #
class Runner:
    @staticmethod
    def run_streamed(agent: Agent, input: List[dict], run_config: RunConfig):
        from asyncio import sleep

        class FakeStreamResult:
            def __init__(self):
                user_input = input[-1]["content"].lower()
                self.final_output = Runner.generate_fake_response(user_input)

            async def stream_events(self):
                for word in self.final_output.split():
                    yield ResponseTextDeltaEvent(delta=word + " ")
                    await sleep(0.03)

        return FakeStreamResult()

    @staticmethod
    def generate_fake_response(user_input: str) -> str:
        if "btc" in user_input:
            return "Bitcoin (BTC): $61,250"
        elif "eth" in user_input:
            return "Ethereum (ETH): $3,450"
        elif "market" in user_input:
            return (
                "📊 Market Update:\n"
                "Bitcoin (BTC): $61,250\n"
                "Ethereum (ETH): $3,450\n"
                "Solana (SOL): $145.60\n"
                "Cardano (ADA): $0.39"
            )
        else:
            return "🤖 Sorry, I can only respond with crypto prices like BTC, ETH, or general market update."
