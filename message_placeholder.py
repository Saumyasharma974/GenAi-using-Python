from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# Create a prompt template with a placeholder
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# Example chat history
chat_history = [
    HumanMessage(content="Hello!"),
    AIMessage(content="Hi there! How can I help you?")
]

# Format the prompt by inserting chat history and new user input
formatted = prompt.format_messages(chat_history=chat_history, input="Tell me about LangChain.")
for msg in formatted:
    print(msg)
