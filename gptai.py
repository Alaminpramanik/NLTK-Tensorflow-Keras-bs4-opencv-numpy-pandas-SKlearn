from transformers import pipeline # First line

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

prompt = "How To Get Sales Leads For Free?"

res = generator(prompt, max_length=50, do_sample=True, temperature=0.9)

print(res[0]['generated_text'])