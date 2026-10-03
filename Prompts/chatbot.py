from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
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

chat_history = [
    SystemMessage(
        content="You are a helpful assistant. You will answer the user's questions to the best of your ability."
    )
]

while True:

    user_input = input("Enter your prompt (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        break

    # Add user message
    chat_history.append(
        HumanMessage(content=user_input)
    )

    # Send entire conversation history
    result = model.invoke(chat_history)

    # Add AI response
    chat_history.append(
        AIMessage(content=result.content)
    )

    print(result.content)


print("Chat History:")

for message in chat_history:
    print(f"{message.type}: {message.content}")
