from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load TinyLlama model and tokenizer
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Create text-generation pipeline
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)

def ask_local_llm(prompt):
    result = pipe(prompt, max_new_tokens=200, do_sample=True, temperature=0.7)
    return result[0]["generated_text"]