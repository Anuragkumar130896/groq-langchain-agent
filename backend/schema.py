from pydantic import BaseModel

class AgentRequest(BaseModel):
    model_provider: str
    model: str
    system_prompt: str
    query: str
    tools: list[str] = []