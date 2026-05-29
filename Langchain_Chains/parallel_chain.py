from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt1 = PromptTemplate(
    template='Write a paragraph notes on the topic of {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate 5 short answer quiz questions on topic of {topic}',
    input_variables=['topic']
)

prompt3 = PromptTemplate(
    template='Merge the given notes and quiz in a single document \n notes -> {notes} and quiz => {quiz}',
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model | parser,
    'quiz': prompt2 | model | parser
})

chain2 = prompt3 | model | parser

chain = parallel_chain | chain2

result = chain.invoke({'topic':"unemployement"})

print(result)

chain.get_graph().print_ascii()
