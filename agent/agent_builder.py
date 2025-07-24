
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, Tool
from dotenv import load_dotenv
import os

load_dotenv()

def get_agent():
    groq_key = os.getenv("GROQ_API_KEY")
    tavily_key = os.getenv("TAVILY_API_KEY")

    # Init LLM
    llm = ChatGroq(
        groq_api_key=groq_key,
        model="llama3-8b-8192"
    )

    # Example tool
    def search_tool(query: str):
        # Call Tavily here (mocked for now)
        return f"Search result for: {query}"

    tools = [
        Tool(
            name="TavilySearch",
            func=search_tool,
            description="Use this tool to search current events."
        )
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent_type="openai-functions",
        verbose=True,
        max_iterations=10,
        max_execution_time=120,
        return_intermediate_steps=True   # 🧪 DEBUGGING
    )
    return agent
