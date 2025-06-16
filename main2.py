# filename: app.py

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, set_seed

# Initialize generator
generator = pipeline("text-generation", model="gpt2")
set_seed(42)  # Optional for reproducibility

# {"text": "some prompt here"}
# Input schema
class Item(BaseModel): 
    text: str

app = FastAPI()

@app.get("/")
def home():
    return {"Message":"Hallo this is home for generate text"}

@app.post("/api/generate")
def generate_text(item: Item):
    outputs = generator(
        item.text, # Prompt
        max_length=100, # Maksimum Promt adalah 100 token
        num_return_sequences=3, # Text yang diberikan adalah 3 luaran teks, dengan prompt yang sama
        no_repeat_ngram_size=2, # No repeat 2 kata dalam bersamaan, e.g dia adalah dan dia adalah
        do_sample=True, # Parameter random untuk prediksi token berikutnya berdasarkan probabilitas terbesar
        top_k=50, # Mengambil 50 top best token
        top_p=0.95 # Mengakomodir token-token kecil probabilitas kumulatif 0.95 -> teks lebih kreatif
    )
    results = [out["generated_text"] for out in outputs]
    return {"message": "Text generated!", "generated_text": results}
