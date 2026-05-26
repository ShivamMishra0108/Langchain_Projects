from langchain_core.prompts import PromptTemplate
import os


template = PromptTemplate(
   template=""" 
    
    You are an expert educational assistant.

    Your task is to explain an exam paper in a clear, structured, and informative way.

    Guidelines:
    - Analyze the paper carefully.
    - Explain the overall pattern and difficulty level.
    - Mention important topics and subject areas covered.
    - Describe the marking scheme if visible.
    - Highlight repeated concepts or frequently asked topics.
    - Give preparation tips for students.
    - Keep the response in the requested style and length.
    - Use headings and bullet points when useful.

    Exam Paper:
    {paper_input}

    Response Style:
    {style_input}

    Response Length:
    {length_input}

    Now provide a detailed explanation and analysis of the exam paper.

        """,

    input_variables=['paper_input','style_input','length_input'],
    validate_template=True
)

template.save('template.json')

print(os.getcwd())
