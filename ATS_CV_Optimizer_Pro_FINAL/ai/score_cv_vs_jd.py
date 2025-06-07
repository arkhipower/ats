
from .ollama_client import query_ollama

def score_cv_vs_jd(cv_text: str, jd_text: str, model: str = None) -> str:
    prompt = f"""You are an AI resume evaluator.

Compare the following resume and job description. Provide:
1. A score from 0 to 100 (how well the CV matches the JD)
2. 3 reasons for the score
3. 3 missing skills or mismatches

[CV]
{cv_text}

[Job Description]
{jd_text}

Output format:
Score: XX/100
Reasons:
- ...
Missing:
- ...
"""
    return query_ollama(prompt, model=model)