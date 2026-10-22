from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


prompt1 = PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate a 5 points summary from the following text\n {text}",
    input_variables=['text']
)

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0.5,
    num_predict=256
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model| parser

result = chain.invoke({"topic":"Artificial Intelligence"})

print(result)

chain.get_graph().print_ascii()