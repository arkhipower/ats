
from core.parsers import extract_text
import os

def test_txt_extraction():
    path = "tests/sample_resume.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write("This is a test CV with keyword: Python")
    text = extract_text(path)
    assert "Python" in text
    os.remove(path)
