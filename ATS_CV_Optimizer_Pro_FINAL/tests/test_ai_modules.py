
from ai.white_keywords_generator import generate_white_keywords
from ai.resume_optimizer import optimize_cv
from ai.resume_auditor import generate_audit

sample_cv = """Experienced safety engineer in oil & gas industry. Familiar with ISO 45001, confined space, PTW."""
sample_jd = """Looking for a candidate with strong HSE background, knowledge in NEBOSH, SIMOPS, PTW, and Aramco GI standards."""
industry = "Oil & Gas"

def test_white_keywords():
    result = generate_white_keywords(sample_cv, industry)
    assert isinstance(result, list) or isinstance(result, str)

def test_optimize_cv():
    result = optimize_cv(sample_cv, sample_jd)
    assert isinstance(result, str) and len(result) > 20

def test_audit():
    result = generate_audit(sample_cv, sample_jd)
    assert "ATS Score" in result
