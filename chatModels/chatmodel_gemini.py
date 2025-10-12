from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.7, max_output_tokens=1024)

result=model.invoke("Write a poem about the sea.")
print(result.content)