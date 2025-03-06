import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load API keys securely
os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
os.environ["LANGCHAIN_API_KEY"] = st.secrets["LANGCHAIN_API_KEY"]
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Cache the model for faster responses
@st.cache_resource
def load_model():
    return ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.5)

llm = load_model()
output_parser = StrOutputParser()

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the queries."),
        ("user", "Question: {question}")
    ]
)

# Create LangChain chain
chain = prompt | llm | output_parser

# Streamlit UI
st.title('LangChain Demo')
input_text = st.text_input("Search the topic")

if input_text:
    with st.spinner("Thinking..."):
        response = chain.invoke({'question': input_text})
    st.write(response)
