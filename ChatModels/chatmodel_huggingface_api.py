from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
load_dotenv()
llm = HuggingFaceEndpoint(
     repo_id="Qwen/Qwen2.5-7B-Instruct",
     task="text-generation",
     provider="featherless-ai",
     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)
model = ChatHuggingFace(llm=llm)

result = model.invoke(input("Hey user enter your query:"))

print(result.content)