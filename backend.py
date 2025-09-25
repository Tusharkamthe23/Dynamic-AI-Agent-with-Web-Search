from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from ai_agent import get_response_from_ai_agent
import os

# Allowed models
ALLOWED_MODEL_NAMES = [
    "llama3-70b-8192",
    "mixtral-8x7b-32768",
    "llama-3.3-70b-versatile",
    "gpt-4o-mini"
]

# FastAPI app
app = FastAPI(title="LangGraph AI Agent")

# Pydantic models
class Message(BaseModel):
    role: str
    content: str

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[Message]
    allow_search: bool

# Chat endpoint
@app.post("/chat")
def chat_endpoint(request: RequestState): 
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model"}
    
    state_messages = [{"role": "system", "content": request.system_prompt}] + [
        {"role": msg.role, "content": str(msg.content)} for msg in request.messages
    ]

    response = get_response_from_ai_agent(
        llm_id=request.model_name,
        messages=state_messages,
        allow_search=request.allow_search,
        provider=request.model_provider
    )
    return {"response": response}

# Run app
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
