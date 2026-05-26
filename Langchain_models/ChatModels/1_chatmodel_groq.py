from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    #api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7,  # Temprature is a paramter used to cutiomize the output
)

response = model.invoke("Tell a poem on cricket in hindi language")
print(response.content)