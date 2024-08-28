import hashlib

def hash_text(text):
    # Create a SHA256 hash object
    sha256_hash = hashlib.sha256()

    # Convert the text to bytes and update the hash object
    sha256_hash.update(text.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hashed_text = sha256_hash.hexdigest()

    return hashed_text

# Get the text input from the user
text = input("Enter the text to hash: ")

# Hash the text and display the result
hashed_text = hash_text(text)
print("Hashed text:", hashed_text)