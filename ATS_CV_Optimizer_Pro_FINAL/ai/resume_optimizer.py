
from ai.ollama_client import query_ollama
from pathlib import Path

PROMPT_FILE = Path(__file__).parent.parent / "prompts" / "prompt_rewrite.txt"

def optimize_cv(cv_text: str, jd_text: str) -> str:
    prompt = PROMPT_FILE.read_text(encoding="utf-8")
    full_prompt = prompt.replace("{{cv_text}}", cv_text).replace("{{jd_text}}", jd_text)
    return query_ollama(full_prompt)
