from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="mistralai/Mistral-7B-Instruct-v0.3",  
#     task="text-generation",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
#     max_new_tokens=200,
# )

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)


template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_vairables = ['topic']
)

template2 = PromptTemplate(
    template="Write a 5 line summary on following text: /n {text}",
    input_variables=['text']

)

prompt1 = template1.invoke({'topic':'Black Hole'})

result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result1.content})

result2 = model.invoke(prompt2)

print(result2.content)

