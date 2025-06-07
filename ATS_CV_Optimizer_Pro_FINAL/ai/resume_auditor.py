
from ai.ollama_client import query_ollama
from pathlib import Path

def generate_audit(cv_text: str, jd_text: str, mode: str = "consultant", model: str = None) -> str:
    PROMPT_MAP = {
    from pathlib import Path
    "consultant": Path(__file__).parent.parent / "prompts" / "prompt_audit_consultant.txt",
        "client": "prompts/prompt_audit_client.txt",
        "self": "prompts/prompt_audit_self_audit.txt",
        "compare": "prompts/prompt_compare_cv_jd.txt",
        "optimize": "prompts/prompt_audit_optimization.txt"
    }
    prompt_path = Path(__file__).parent.parent / PROMPT_MAP[mode]
    prompt = prompt_path.read_text(encoding="utf-8")
    full_prompt = (
        prompt.replace("{{cv_text}}", cv_text)
              .replace("{{jd_text}}", jd_text)
              .replace("{{role}}", "HSE Manager")
              .replace("{{context}}", "Oil & Gas project safety leadership")
              .replace("{{found_keywords}}", "")
              .replace("{{missing_keywords}}", "")
    )
    return query_ollama(full_prompt, model=model)