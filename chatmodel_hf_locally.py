from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

print("Loading model...")
llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    device_map='cpu',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
print("Model loaded, creating ChatHuggingFace...")
model = ChatHuggingFace(llm=llm)

print("Invoking model...")
result = model.invoke("Who is Virat Kohli?")

print(result.content)