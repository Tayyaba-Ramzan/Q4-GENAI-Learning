<h1 align="center">🚀 CryptoDataAgent</h1>

<p align="center">
  <em>An intelligent crypto assistant that speaks market fluently — powered by AI, built by a developer who means business.</em><br><br>
  <img src="https://img.shields.io/badge/Built%20With-Chainlit%20%26%20Gemini-6e40c9?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Made%20By-Tayyaba%20Ramzan-ff69b4?style=for-the-badge">
</p>

---

## ✨ What is CryptoDataAgent?

`CryptoDataAgent` is a blazing-fast, real-time **crypto assistant** that uses **Chainlit** for chat UI and **Gemini API** as the brain behind the bot.  
It fetches **live crypto prices** via the [Coinlore API](https://www.coinlore.com/) and lets users interact with the market using natural language — no more opening charts or refreshing dashboards.

> 💬 _“What’s the current price of ETH?”_  
> 🧠 _CryptoDataAgent responds instantly with live data._

---

## 🧠 Features at a Glance

| Feature                        | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| 📡 Live Market Data           | Pulls real-time crypto prices from Coinlore API                             |
| 🤖 Conversational Chat Agent  | AI agent with tool-function integration for crypto-specific replies         |
| 🔐 API Security               | Sensitive keys are handled using `.env` and `python-dotenv`                 |
| ⚙️ Modular Agent Architecture | Clean separation between agent logic, tools, and runner                     |
| 🚀 Streamed Output            | Typing animation via Chainlit's token streaming                             |
| 🧩 Easy Extensibility         | Add more tools or models without breaking the base structure                |

---

## 💬 Example Chat

```plaintext
User: market prices  
Assistant:
📊 Top 10 Crypto Prices:
- Bitcoin (BTC): $63,012
- Ethereum (ETH): $3,492
- Solana (SOL): $134.21
...

✅ Also supports specific queries: “Show me BTC and XRP prices”

🚀 Quick Start

# Clone the repository
git clone https://github.com/Tayyaba-Ramzan/Crypto-Data-Agent.git
cd crypto-data-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add your Gemini API key to .env
cp .env.example .env
# Edit .env file and paste your key like:
# GEMINI_API_KEY=your_gemini_api_key_here

# Run the app
chainlit run main.py


🔐 Environment Variables
Create a .env file in the root directory:
GEMINI_API_KEY=your_gemini_api_key_here

📁 Project Structure
crypto-data-agent/
│
├── agents/
│   ├── agents.py           # Custom classes: Agent, Runner, decorators
│   └── __init__.py         # Package marker
│
├── main.py                 # Main entry point with Chainlit logic
├── .env.example            # Sample .env file
├── requirements.txt        # Python dependencies
└── README.md               # This file 🔥

📦 Tech Stack
Language: Python 3.9+

Chat Framework: Chainlit

LLM Provider: Gemini (Google)

Crypto API: Coinlore

Config Management: dotenv

🔭 Roadmap
 ✅ Real-time crypto fetching

 🔍 Coin-specific filtering by name/symbol

 📈 Add 24h change, volume, and ranking

 📊 Add graph-based visualization with Plotly

 🌐 Deploy on Vercel / Streamlit Cloud

Tayyaba Ramzan
💻 Passionate about building AI-powered tools that simplify life
📫 Email: tayyabaramzan.it@gmail.com
🐙 GitHub: @Tayyaba-Ramzan

🛡️ License
Licensed under the MIT License.
See LICENSE for more details.

🌟 Star This Repo
If this project helped you or inspired you — don’t forget to ⭐ star the repo!
Let the world know what clean and smart AI looks like.

“Crypto intelligence meets conversational interface — say hello to the future of market analysis.”
