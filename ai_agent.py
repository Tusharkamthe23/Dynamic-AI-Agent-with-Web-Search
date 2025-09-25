from dotenv import load_dotenv
load_dotenv()

import os
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

# Load API keys
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Prebuilt search tool
search_tool = TavilySearchResults(max_results=2)

def get_response_from_ai_agent(llm_id, messages, allow_search, provider):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)
    else:
        raise ValueError("Invalid provider")

    tools = [TavilySearchResults(max_results=2)] if allow_search else []
    agent = create_react_agent(model=llm, tools=tools)

    state = {"messages": messages}
    response = agent.invoke(state)
    
    all_messages = response.get("messages", [])
    ai_messages = [m.content for m in all_messages if isinstance(m, AIMessage)]
    return ai_messages[-1] if ai_messages else None
