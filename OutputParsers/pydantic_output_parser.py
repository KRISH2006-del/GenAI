from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0.5,
    num_predict=256
)

class Person(BaseModel):
    name: str = Field(..., description="The person's name")
    age: int = Field(..., gt=18,description="The person's age")
    city: str = Field(..., description="The city where the person lives")


parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = "generate the name, age and city of a fictional {place} person. \n {format_instruction}",
    input_variables=["place"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

prompt = template.invoke({"place": "New York"})

print("Prompt:", prompt)

result = model.invoke(prompt)

parsed_result = parser.parse(result.content)


print("Parsed Result:", parsed_result)