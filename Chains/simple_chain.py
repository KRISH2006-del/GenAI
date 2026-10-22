from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate(
    template="Generate 5 intresting facts about {topic}.",
    input_variables=["topic"],
)

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0.5,
    num_predict=256
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic": "cars"})

print(result)

chain.get_graph().print_ascii()