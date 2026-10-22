from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0.5,
    num_predict=256
)

parser = JsonOutputParser()

template = PromptTemplate(
    template = "Give me 5 facts about {topic} \n{format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = template | model | parser

model_response = chain.invoke(input={"topic": "Black holes"})

print("Model Response:", model_response)
