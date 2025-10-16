from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

chat_history=[
    SystemMessage(content="You are a helpful assistant."),
] 

while True :
    input_text=input("You: ")
    chat_history.append(HumanMessage(content=input_text))
    if input_text.lower() in ["exit", "quit"]:
        break
    response=model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content if hasattr(response, "content") else response))
    print("Bot:", response.content if hasattr(response, "content") else response)

print(chat_history)