# filename: app.py

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, set_seed

# Initialize generator
generator = pipeline("text-generation", model="gpt2")
set_seed(42)  # Optional for reproducibility

# Input schema
class Item(BaseModel):
    text: str

app = FastAPI()

@app.post("/api/generate")
def generate_text(item: Item):
    outputs = generator(
        item.text,
        max_length=100,
        num_return_sequences=3,
        no_repeat_ngram_size=2,
        do_sample=True,
        top_k=50,
        top_p=0.95
    )
    results = [out["generated_text"] for out in outputs]
    return {"message": "Text generated!", "generated_text": results}
