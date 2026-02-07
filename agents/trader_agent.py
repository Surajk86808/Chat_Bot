from crewai import Agent, LLM
import os
from dotenv import load_dotenv

load_dotenv()

# ✅ Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is required. Add it to your .env file.")


############################################
# Gemini LLM Config
############################################

model_client = LLM(
    model="gemini/gemini-2.0-flash", 
    api_key=GEMINI_API_KEY,
    temperature=0.2,                  
    max_tokens=2048
)


############################################
# Trader Agent
############################################

trader_agent = Agent(
    role="Strategic Stock Trader",
    goal=(
        "Decide whether to Buy, Sell, or Hold a given stock based on live market data, "
        "price movements, and financial analysis."
    ),
    backstory=(
        "You are a strategic trader with years of experience in timing market entry and exit points. "
        "You rely on real-time stock data, daily price movements, and volume trends to optimize returns and reduce risk."
    ),
    llm=model_client,
    tools=[],   
    verbose=True,
)
