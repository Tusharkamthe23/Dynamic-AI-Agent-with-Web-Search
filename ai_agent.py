# if you dont use pipenv uncomment the following:
from dotenv import load_dotenv
load_dotenv()

#Step1: Setup API Keys for Groq, OpenAI and Tavily
import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

#Step2: Setup LLM & Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

openai_llm=ChatOpenAI(model="gpt-4o-mini")
groq_llm=ChatGroq(model="llama-3.3-70b-versatile")

search_tool=TavilySearchResults(max_results=2)

#Step3: Setup AI Agent with Search tool functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt="Act as an AI chatbot who is smart and friendly"

def get_response_from_ai_agent(llm_id, messages, allow_search, provider):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)

    tools = [TavilySearchResults(max_results=2)] if allow_search else []
    agent = create_react_agent(model=llm, tools=tools)

    state = {"messages": messages}

    response = agent.invoke(state)
    all_messages = response.get("messages")
    ai_messages = [m.content for m in all_messages if isinstance(m, AIMessage)]
    return ai_messages[-1] if ai_messages else None

''''llm_id="llama-3.3-70b-versatile"
query="what is apple"
allow_search=True
provider="Groq'''
#response=get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
#print(response)