KEY = "my_encryption_key"

def xor_cipher(text: str, key: str) -> str:
    output = ""

    for i in range(len(text)):
        encrypted_character = chr(ord(text[i]) ^ ord(key[i % len(key)]))
        output = output + encrypted_character

    return output

if __name__ == "__main__":
    key = KEY

    message = input("Enter the message to encrypt: ")

    cipher_text = xor_cipher(message, key)
    print(f"Cipher text: {cipher_text.encode().hex()}")

    plain_text = xor_cipher(cipher_text, key)
    print(f"Plain text: {plain_text}")