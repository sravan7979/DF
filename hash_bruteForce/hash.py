import hashlib

message = "123"
hash_value = hashlib.md5(message.encode()).hexdigest()

print("Hash:", hash_value)

