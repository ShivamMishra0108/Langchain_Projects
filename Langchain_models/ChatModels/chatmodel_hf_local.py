from langchain_huggingface  import ChatHuggingFace, HuggingFacePipeline
import os

llm = HuggingFacePipeline.from_model_id(
    model_id="mistralai/Mistral-7B-Instruct-v0.1",
    task = "text-generation",
    pipeline_kwargs=dict(
        temprature=0.5,
        max_new_tokens = 100
    )
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is capital of india")

print(result.content)