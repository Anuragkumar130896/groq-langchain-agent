import streamlit as st
import requests

st.title("Chat bot with Groq + Tavily")

provider = st.text_input("Model Provider", "Groq")
model = st.text_input("Model Name", "llama3-8b-8192")
prompt = st.text_area("System Prompt", "You are a helpful assistant.")
query = st.text_input("Ask your question")

if st.button("Ask"):
    payload = {
        "model_provider": provider,
        "model": model,
        "system_prompt": prompt,
        "query": query
    }

    response = requests.post("http://localhost:8000/query", json=payload)
    st.write(" AI Response:")
    st.success(response.json()["response"])
