from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0.5,
    num_predict=256
)

# 1st prompt -> detailed report 
template1 = PromptTemplate(
    template="Please provide a detailed report on the following topic: {topic}",
    input_variables=["topic"]
)

# 2nd prompt -> summary of the report
template2 = PromptTemplate(
    template="Please provide a 5 line summary of the following report: {text}",
    input_variables=["text"]
)

prompt1 = template1.invoke({"topic": "black holes"})

result = model.invoke(prompt1)

print(result.content)

prompt2 = template2.invoke({"text": result.content})

result2 = model.invoke(prompt2)

print(result2.content)