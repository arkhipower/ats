import hashlib

VALID_LICENSE_HASHES = [
    "9dffbf69ffba8bc38bc4e01abf4b1675",  # example hash for key: DEMO-KEY-123
]

def check_license_key(user_key: str) -> bool:
    key_hash = hashlib.md5(user_key.encode("utf-8")).hexdigest()
    return key_hash in VALID_LICENSE_HASHES