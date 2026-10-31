from hashlib import sha1

def git_hash(text):
    data = text.encode()
    head = f"blob {len(data)}\0"
    full = head.encode() + data
    return sha1(full).hexdigest()

print(git_hash("hello\n"))
