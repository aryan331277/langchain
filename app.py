from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate#for creating chatbot
from langchain_core.output_parsers import StrOutputParser#default output parser

import streamlit as st
import os
from dotenv import load_dotenv


os.environ['GEMINI_API_KEY']=os.getenv('GEMINI_API_KEY')
os.environ['LANGCHAIN API KEY']=os.environ['LANGCHAIN API KEY']
#Langsmith
os.environ['LANGCHAIN_TRACING_V2']="true"

#prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the queries.")
        ("user","Question:{question}")
    ]
)
#streamlit
st.title('Langchain Demo')
input_text=st.text_input("Search the topic")
#LangChain provides you features which you can attach in  the form of chain
#output
llm=ChatGoogleGenerativeAI(model="gemini-pro")
output_parser=StrOutputParser
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
