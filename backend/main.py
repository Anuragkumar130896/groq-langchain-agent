from fastapi import FastAPI
from models.request_schema import AgentRequest
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

@app.post("/query")
def handle_query(request: AgentRequest):
    # Optional: Print received fields
    print("Received:", request.model, request.query)

    # Setup LLM using dynamic fields
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name=request.model  # e.g., "llama3-8b-8192"
    )

    # Combine system prompt + user query
    full_prompt = f"{request.system_prompt}\n\n{request.query}"

    response = llm.invoke(full_prompt)
    return {"response": response}
