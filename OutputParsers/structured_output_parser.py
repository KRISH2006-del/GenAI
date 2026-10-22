from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0.5,
    num_predict=256
)

schema = [
    ResponseSchema(name="fact_1", description = "fact 1 about the topic"),
    ResponseSchema(name="fact_2", description = "fact 2 about the topic"),
    ResponseSchema(name="fact_3", description = "fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = "Give me 3 facts about {topic} \n{format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = template | model | parser

model_response = chain.invoke(input={"topic": "Black holes"})

print("Model Response:", model_response)