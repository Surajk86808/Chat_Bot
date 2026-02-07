# 🤖 StockCrew AI - Multi-Agent Stock Trading System

An intelligent multi-agent system powered by CrewAI and Google Gemini that analyzes stock market data and provides actionable trading recommendations.

## 🌟 Features

- **Multi-Agent Architecture**: Specialized AI agents working together
  - 📊 **Analyst Agent**: Performs in-depth stock analysis using real-time market data
  - 💼 **Trader Agent**: Makes strategic Buy/Sell/Hold decisions based on analysis
  
- **Real-Time Market Data**: Fetches live stock prices and metrics using Yahoo Finance
- **AI-Powered Insights**: Leverages Google Gemini 2.0 Flash for intelligent decision-making
- **Automated Workflow**: Seamless task orchestration between agents

## 🏗️ Architecture

```
┌─────────────────────┐
│   User Input        │
│   (Stock Symbol)    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────────────┐
│         Stock Crew                  │
│  ┌────────────────────────────┐    │
│  │   Analyst Agent            │    │
│  │   - Fetches stock data     │    │
│  │   - Analyzes trends        │    │
│  │   - Provides insights      │    │
│  └──────────┬─────────────────┘    │
│             │                       │
│             ▼                       │
│  ┌────────────────────────────┐    │
│  │   Trader Agent             │    │
│  │   - Reviews analysis       │    │
│  │   - Makes trade decision   │    │
│  │   - Recommends action      │    │
│  └────────────────────────────┘    │
└─────────────────────────────────────┘
           │
           ▼
┌─────────────────────┐
│   Trading Report    │
│   (Buy/Sell/Hold)   │
└─────────────────────┘
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Google Gemini API Key
- Internet connection for real-time data

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/stockcrew-ai.git
   cd stockcrew-ai
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

   To get a Gemini API key:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Sign in with your Google account
   - Generate a new API key

### Usage

Run the main script with a stock symbol:

```python
# Edit main.py to change the stock symbol
python main.py
```

**Example Output:**
```
Stock: TSLA
Price: 245.32 USD
Change: +5.67 (+2.37%)

Analysis Summary:
- Current Price: Strong upward momentum
- Volume: Above average trading activity
- Recommendation: BUY - Positive trend indicators

Trading Decision: BUY
```

## 📁 Project Structure

```
stockcrew-ai/
├── agents/
│   ├── analyst_agent.py      # Financial analysis agent
│   └── trader_agent.py        # Trading decision agent
├── tasks/
│   ├── analyse_task.py        # Stock analysis task definition
│   └── trade_task.py          # Trading decision task definition
├── tools/
│   └── stock_research_tool.py # Yahoo Finance integration
├── crew.py                    # Crew orchestration
├── main.py                    # Entry point
├── requirements.txt           # Python dependencies
├── .env                       # API keys (not in repo)
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## 🛠️ Components

### Agents

#### Analyst Agent
- **Role**: Financial Market Analyst
- **Tools**: Live Stock Information Tool (Yahoo Finance)
- **Temperature**: 0.3 (balanced creativity/consistency)
- **Function**: Analyzes stock performance, trends, and key metrics

#### Trader Agent
- **Role**: Strategic Stock Trader
- **Tools**: None (uses analysis from Analyst Agent)
- **Temperature**: 0.2 (more deterministic)
- **Function**: Makes Buy/Sell/Hold recommendations

### Tools

#### Live Stock Information Tool
- Fetches real-time stock data from Yahoo Finance
- Returns: Current price, daily change, percentage change
- Parameters: Stock ticker symbol (e.g., AAPL, TSLA, MSFT)

## 🧪 Example Notebook

The project includes `pydantic_agentic_ai.ipynb` demonstrating:
- Pydantic AI agent creation
- Weather forecast tool integration (example)
- Async execution patterns

## 🔧 Customization

### Changing the Stock Symbol

Edit `main.py`:
```python
if __name__ == "__main__":
    run("AAPL")  # Change to any valid ticker
```

### Adjusting Agent Behavior

Modify temperature settings in agent files:
```python
model_client = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=GEMINI_API_KEY,
    temperature=0.3,  # Lower = more deterministic
    max_tokens=2048
)
```

### Adding New Tools

Create a new tool in `tools/`:
```python
from crewai.tools import tool

@tool("Your Tool Name")
def your_tool(param: str) -> str:
    """Tool description"""
    # Implementation
    return result
```

## 📊 Supported Stock Symbols

Any stock symbol available on Yahoo Finance, including:
- US Stocks: AAPL, GOOGL, MSFT, TSLA, AMZN
- Indian Stocks: RELIANCE.NS, TCS.NS, INFY.NS
- Crypto: BTC-USD, ETH-USD

## ⚠️ Disclaimer

**This tool is for educational and research purposes only.**

- Not financial advice
- Always do your own research
- Consult a licensed financial advisor before making investment decisions
- Past performance doesn't guarantee future results
- The developers are not responsible for any financial losses

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CrewAI](https://www.crewai.com/) - Multi-agent framework
- [Google Gemini](https://deepmind.google/technologies/gemini/) - AI model
- [yfinance](https://github.com/ranaroussi/yfinance) - Yahoo Finance data
- [LiteLLM](https://github.com/BerriAI/litellm) - LLM integration

## 📧 Contact

Suraj Kumar - [@yourhandle](https://twitter.com/yourhandle)

Project Link: [https://github.com/yourusername/stockcrew-ai](https://github.com/yourusername/stockcrew-ai)

---

**⭐ If you found this project helpful, please give it a star!**
