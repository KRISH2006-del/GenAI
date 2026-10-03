from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert.'),
    ('human', 'Explain {topic} in simple terms.')
])

prompt = chat_template.invoke({ "domain": "AI", "topic": "machine learning" })

print(prompt)