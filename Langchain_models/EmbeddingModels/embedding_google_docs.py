from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

document = (
    "Delhi is capital of India",
    "Kolkata is capital of WB",
    "Paris is capital of France",
)

result = embedding.embed_query(document)

print(str(result))