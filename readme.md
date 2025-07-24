# chat bot using Groq + LLaMA3 + FastAPI + Streamlit

This project is an end-to-end conversational AI agent that uses the **LLaMA3-8B-8192 model** through **Groq’s ultra-fast inference engine**. It’s built using a FastAPI backend to process structured queries and a Streamlit frontend for a simple UI.

---

##Features

- Query a powerful LLaMA3 AI model using Groq
- Send dynamic prompts with `model`, `provider`, and `system_prompt`
- FastAPI backend with RESTful `/query` endpoint
- Streamlit frontend for easy interaction
- Runs locally using `uvicorn` and `streamlit`
- Modular and scalable project structure

---

##  Tech Stack

- **LLM**: Groq API + LLaMA3 8B
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Others**: Pydantic, Uvicorn, dotenv

---

##  Project Structure

ai_agent_app/
├── backend/
│ └── main.py # FastAPI backend entrypoint
├── models/
│ └── request_schema.py # Pydantic model for request body
├── agent/
│ └── agent_builder.py # (optional) tool-based agent
├── frontend/
│ └── app.py # Streamlit UI
├── .env # API keys
├── requirements.txt # Python dependencies
├── README.md # Project documentation


---

## Setup Instructions

###  Step 1: Clone Repo & Install Requirements

```bash
git clone https://github.com/your-username/ai-agent-app.git
cd ai-agent-app
python -m venv venv
venv\Scripts\activate  # For Windows
# Or use `source venv/bin/activate` for Mac/Linux

pip install -r requirements.txt

Step 2: Create .env File
GROQ_API_KEY=your_groq_api_key_here
You can get the API key here: https://console.groq.com/keys

 Step 3: Run FastAPI Backend
uvicorn backend.main:app --reload
 Visit API docs at:
http://127.0.0.1:8000/docs

Sample /query request body:
{
  "model_provider": "groq",
  "model": "llama3-8b-8192",
  "system_prompt": "You are a helpful assistant.",
  "query": "What is Artificial Intelligence?"
}
 Step 4: Run Streamlit Frontend
cd frontend
streamlit run app.py
🖥 Visit your frontend at:
http://localhost:8501


###Future Enhancements

 #Add tool-calling with Tavily web search

# Model switcher (Groq / OpenAI / Hugging Face)

# Chat history memory

# Deployment to Hugging Face or Render


# Acknowledgements
Meta AI – LLaMA3

Groq Inference Cloud

FastAPI Docs

Streamlit Docs

LangChain


