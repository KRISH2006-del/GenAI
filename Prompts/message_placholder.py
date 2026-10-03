from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#chat template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer service  expert.'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

chat_history = []
#load chat history
with open('chat_history.txt', 'r') as f:
    for line in f:
        chat_history.append(line.strip())

print("Chat History:")
print(chat_history)


#create prompt
chat_prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'What is the status of my order?'})
print("chat_prompt:", chat_prompt)