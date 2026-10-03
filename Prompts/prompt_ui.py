from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
llm = HuggingFaceEndpoint(
     repo_id="Qwen/Qwen2.5-7B-Instruct",
     task="text-generation",
     provider="featherless-ai",
     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)
model = ChatHuggingFace(llm=llm)
st.header("Chat with Qwen2.5-7B-Instruct Model")

user_input = st.text_input("Enter your prompt:")

if st.button("Submit"):
    result = model.invoke(user_input)
    st.write(result.content)