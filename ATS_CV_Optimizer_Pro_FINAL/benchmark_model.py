
import time
from ai.ollama_client import query_ollama

prompt = "What are 3 key responsibilities of an HSE Manager in the oil & gas sector?"

models = ["llama3:8b", "mistral:7b-instruct"]
results = {}

for model in models:
    print(f"\nRunning model: {model}")
    start = time.time()
    response = query_ollama(prompt, model=model)
    duration = round(time.time() - start, 2)
    results[model] = {"response": response, "time": duration}
    print(f"Time: {duration}s\nResponse:\n{response[:500]}...\n")

with open("benchmark_output.txt", "w", encoding="utf-8") as f:
    for model, result in results.items():
        f.write(f"=== {model} ===\n")
        f.write(f"Time: {result['time']}s\n")
        f.write(f"Response:\n{result['response']}\n\n")
