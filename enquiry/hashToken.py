import hashlib

def generate_request_hash(data, ip, user_agent):
    raw = f"{data['email']}{data['phone']}{ip}{user_agent}"
    return hashlib.sha256(raw.encode()).hexdigest()
