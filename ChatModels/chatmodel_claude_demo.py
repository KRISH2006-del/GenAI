from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

model = ChatAnthropic(model="claude-3-opus-20241209", temperature=0.7, max_completion_tokens=100)

model_result = model.invoke("What is the capital of France?")
print(model_result.content)