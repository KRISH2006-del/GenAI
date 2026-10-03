from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

chat_model = ChatOpenAI(model="gpt-4", temperature=0.7, max_completion_tokens=100)

chat_result = chat_model.invoke("What is the capital of France?")
print(chat_result)