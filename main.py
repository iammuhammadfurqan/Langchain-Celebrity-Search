## Integrate Our Code with Openai API
import os
from constant import openai_api_key
from langchain.llms import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_api_key

# StreamLit framework 

st.title("Langchain Demo with OpenAI API")
input_text = st.text_input("Search the Topic you want")

##OPENAI_LLMS

llm = OpenAI(temperature = 0.8)

if input_text:
    st.write(llm(input_text))