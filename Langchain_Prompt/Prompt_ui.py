from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

st.header("Research Tab")

paper_input = st.selectbox("Select Exam Name",["UPSC","NDA","JEE","NEET","SSC","GATE","CAT","AGNIVEER"])

style_input = st.selectbox("Select Explaination style",["Beginner-Friendly","Oriented","Detailed"," mathematical"])

length_input = st.selectbox("Select Explaination length",["Short(1-2 Paragrph)","Medium(3-5 Paragrph)","Detailed Explaination"])

template = load_prompt('template.json')

prompt = template.invoke({
   'paper_input':paper_input,
   'style_input':style_input,
   'length_input':length_input
})

if st.button("Summarize"):
   result = model.invoke(prompt)
   st.write(result.content)