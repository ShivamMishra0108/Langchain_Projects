from typing import Literal
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model2 = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
model = ChatGroq(model="llama-3.1-8b-instant") 

parser1 = StrOutputParser()

class Feedback(BaseModel):

    sentiment: Literal['positive', 'negative'] = Field(description="Give the sentiment of the output")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Generate the positive or negative sentiment of the feedback that is {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template="Write an appropriate response to the positive feedback \n {feedback}",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to the negative feedback \n {feedback}",
    input_variables=['feedback']
)

classifier_chain = prompt1 | model | parser2

branch_Chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser1 ),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser1 ),
    RunnableLambda(lambda x:'could not find sentiment')
)

chain = classifier_chain | branch_Chain

print(chain.invoke({'feedback': "This is a beautiful phone" }))

chain.get_graph().print_ascii()


