from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional
import os

load_dotenv()

model = ChatOllama(
    model="qwen2.5:7b",
    temperature=0.5
)



#schema for the structured output
class ReviewSummary(TypedDict):
    key_themes: Annotated[list[str], "A list of key themes or topics mentioned in the review"]
    summary: Annotated[str, "A concise summary of the review"]
    sentiment: Annotated[str, "The overall sentiment of the review (positive, negative, or neutral)"]
    pros: Annotated[Optional[list[str]], "A list of positive aspects or advantages mentioned in the review"]
    cons: Annotated[Optional[list[str]], "A list of negative aspects or disadvantages mentioned in the review"]

structured_model = model.with_structured_output(ReviewSummary)

result = structured_model.invoke("""I recently tried the iPhone Duo, and overall, I’m impressed with its sleek design, smooth performance, and user-friendly interface. The display quality is excellent, and the camera captures clear, detailed photos. Battery life is decent, although it could be better with heavy usage. The device feels premium and responsive, making it a good choice for everyday use. Overall, it offers a satisfying experience, but the price may be a concern for budget-conscious buyers.
""")

print(result)