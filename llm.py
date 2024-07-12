from itertools import chain
from click import prompt
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama
from langchain.document_loaders import DirectoryLoader
import streamlit as st
from langchain_community.document_loaders import PyMuPDFLoader

loader = PyMuPDFLoader(
    "company_data.pdf")
data = loader.load()
data[0]

st.title("Chat with Ollama LLM")
input_txt=st.text_input("Enter your message...")

prompt= ChatPromptTemplate.from_messages([
    ("system","you are a chat HR chat bot. you guide for the HR department queries. you name is Talentship ai"),
    ("user","user query:{query}")
])

llm=ollama.Ollama(model='llama3')
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_txt:
    st.write(chain.invoke({"query":input_txt}))
    

 