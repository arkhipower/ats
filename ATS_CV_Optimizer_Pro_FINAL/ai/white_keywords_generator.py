
from pathlib import Path
import requests
import json

PROMPT_FILE = Path(__file__).parent.parent / "prompts" / "prompt_keywords.txt"

def load_prompt(template_path: Path, cv_text: str, industry: str) -> str:
    prompt = template_path.read_text(encoding="utf-8")
    return prompt.replace("{{industry}}", industry).replace("{{cv_text}}", cv_text)

def generate_white_keywords(cv_text: str, industry: str) -> list:
    full_prompt = load_prompt(PROMPT_FILE, cv_text, industry)
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3",
        "prompt": full_prompt,
        "stream": False
    })
    if response.ok:
        content = response.json().get("response", "")
        try:
            return json.loads(content)
        except Exception:
            return content.strip().split(", ")
    return []
