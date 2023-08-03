## Integrate our code OpenAI API
import os
from langchain.llms import OpenAI

import streamlit as st

#os.environ["OPENAI_API_KEY"]=OPENAI_API_KEY

# streamlit framework

st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")

## OPENAI LLMS
llm=OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))
