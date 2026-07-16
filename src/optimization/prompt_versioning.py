import hashlib
def generate_version(text):
    return hashlib.sha256(text.encode()).hexdigest()[:8]