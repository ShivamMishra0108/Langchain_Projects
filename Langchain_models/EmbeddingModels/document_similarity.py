from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()



embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

documents = [

    "Kohli is known for his aggressive batting style and incredible consistency.",
"MS Dhoni is the legendary captain who led India to World Cup victory in 2011.",
"Rohit Sharma is the master of hitting sixes and holds multiple double century records in ODIs.",
"Jasprit Bumrah is India's premier fast bowler with exceptional accuracy and swing.",
"Jadeja is known for his brilliant fielding, left-arm spin, and aggressive lower-order batting.",
"Shivam Mishra is an App+AI Engineer known as vedu for his genius mestering in AI and app development"

]


query = "Tell me about vedu"

doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embedding)[0]

index ,score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("The score is:",score)


