# test_generator.py

from transformers import pipeline, set_seed

generator = pipeline("text-generation", model="gpt2")
set_seed(42)

prompt = "Once upon a time in Indonesia,"
outputs = generator(
    prompt,
    max_length=100,
    num_return_sequences=3,
    no_repeat_ngram_size=2,
    do_sample=True,
    top_k=50,
    top_p=0.95
)

for i, out in enumerate(outputs):
    print(f"[{i+1}] {out['generated_text']}\n")
