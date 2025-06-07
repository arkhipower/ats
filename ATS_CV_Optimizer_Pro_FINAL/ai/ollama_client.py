import subprocess
import os

MODEL = "llama3:8b"  # Default model, can be changed dynamically
OLLAMA_TIMEOUT = 120

def set_model(model_name):
    global MODEL
    MODEL = model_name

def run_ollama_prompt(prompt: str) -> str:
    try:
        result = subprocess.run(
            ["ollama", "run", MODEL],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=OLLAMA_TIMEOUT
        )
        output = result.stdout.decode("utf-8", errors="ignore")
        return output.strip()
    except Exception as e:
        return f"[ERROR] {str(e)}"

def run_prompt_from_file(file_path, variables: dict) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            prompt = f.read()
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{{{key}}}}}", value.strip())
        return run_ollama_prompt(prompt)
    except Exception as e:
        return f"[ERROR loading prompt] {str(e)}"