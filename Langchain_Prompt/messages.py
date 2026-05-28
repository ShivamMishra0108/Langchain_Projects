from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

messages= [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Give a demo review of a new bought phone")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)