from crewai import Agent, LLM
import os
from dotenv import load_dotenv
from tools.stock_research_tool import get_stock_price

load_dotenv()

# ✅ Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is required. Add it to your .env file.")


############################################
# LLM CONFIG (Gemini)
############################################

model_client = LLM(
    model="gemini/gemini-2.0-flash",   # ⭐ Best for agents
    api_key=GEMINI_API_KEY,
    temperature=0.3,                   # Stable outputs
    max_tokens=2048
)


############################################
# AGENT
############################################

analyst_agent = Agent(
    role="Financial Market Analyst",
    goal=(
        "Perform in-depth evaluations of publicly traded stocks using real-time data, "
        "identify trends, performance insights, and key financial signals to support decision-making."
    ),
    backstory=(
        "You are a veteran financial analyst with deep expertise in stock market data, "
        "technical trends, and company fundamentals. You create structured reports based on live indicators."
    ),
    llm=model_client,
    tools=[get_stock_price],
    verbose=True,
)
