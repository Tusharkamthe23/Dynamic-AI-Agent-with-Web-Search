# if you dont use pipenv uncomment the following:
from dotenv import load_dotenv
load_dotenv()

#Step1: Setup Pydantic Model (Schema Validation)
from pydantic import BaseModel
from typing import List

# Define message schema
class Message(BaseModel):
    role: str
    content: str

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[Message]
    allow_search: bool

#Step2: Setup AI Agent from FrontEnd Request
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES = [
    "llama3-70b-8192",
    "mixtral-8x7b-32768",
    "llama-3.3-70b-versatile",
    "gpt-4o-mini"
]

app = FastAPI(title="LangGraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState): 
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model"}
    
    llm_id = request.model_name
    provider = request.model_provider

    # 🔹 FIX: ensure every message content is a plain string
    state_messages = [{"role": "system", "content": request.system_prompt}] + [
        {"role": msg.role, "content": str(msg.content)} for msg in request.messages
    ]

    # Pass the fixed messages list into your agent
    response = get_response_from_ai_agent(
        llm_id=llm_id,
        messages=state_messages,
        allow_search=request.allow_search,
        provider=provider
    )
    return response

# Run app
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
