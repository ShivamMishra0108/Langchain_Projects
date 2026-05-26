# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# import os

# load_dotenv()  

# api_key = os.getenv("GEMINI_API_KEY")

# llm = ChatGoogleGenerativeAI(
#    model="gemini-2.0-flash",
#     google_api_key=api_key
# )

# response = llm.invoke("What is LangChain?")
# print(response.content)


from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq  

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.1-8b-instant",  
    api_key=groq_api_key,
)

response = llm.invoke("What is the capital of India?")
print(response.content)