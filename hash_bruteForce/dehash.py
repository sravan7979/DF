import hashlib

target_hash = "202cb962ac59075b964b07152d234b70"

for i in range(1000):
    guess = str(i).zfill(3)

    guess_hash = hashlib.md5(
        guess.encode()
    ).hexdigest()

    if guess_hash == target_hash:
        print("Password Found:", guess)
        break
