
from .ollama_client import query_ollama

def generate_cover_letter(cv_text: str, jd_text: str, model: str = None) -> str:
    prompt = f"""You are an expert career assistant.

Based on the following CV and job description, generate a personalized, ATS-friendly cover letter:

[CV]
{cv_text}

[Job Description]
{jd_text}

Format:
- 3 short paragraphs
- Emphasize fit, motivation, and value
- Use formal tone

Return only the cover letter text.
"""
    return query_ollama(prompt, model=model)