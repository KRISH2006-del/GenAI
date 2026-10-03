from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
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

prompt = PromptTemplate(
    template="Explain {topic} in simple terms with an example.",
    input_variables=["topic"]
)

final_prompt = prompt.invoke({
    "topic": "API"
})

result = model.invoke(final_prompt)

print(result.content)