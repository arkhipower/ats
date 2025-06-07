
import hashlib
from pathlib import Path

VALID_KEYS_HASHED = [
    "2bb80d537b1da3e38bd30361aa855686bde0ba97556b25fb4c7c381c91822f0d",  # example: "DEMO-KEY-123"
]

def hash_key(key: str) -> str:
    return hashlib.sha256(key.strip().encode()).hexdigest()

def is_valid_license(input_key: str) -> bool:
    return hash_key(input_key) in VALID_KEYS_HASHED

def read_stored_key() -> str:
    key_path = Path("config/license.key")
    return key_path.read_text().strip() if key_path.exists() else ""

def require_license_key():
    key = read_stored_key()
    if not is_valid_license(key):
        return False
    return True
