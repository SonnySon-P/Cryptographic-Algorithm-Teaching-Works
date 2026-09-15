KEY = "my_encryption_key"

def vigenere_cipher(text: str, key: str, is_decrypt: int) -> str:
    output = ""
    key_index = 0

    for character in text:
        if character.isalpha():
            shift = ord(key[key_index % len(key)].upper()) - ord("A")

            if is_decrypt:
                shift = -shift

            if character.isupper():
                output += output + chr((ord(character) - ord("A") + shift) % 26 + ord("A"))
            else:
                output = output + chr((ord(character) - ord("a") + shift) % 26 + ord("a"))

            key_index = key_index + 1
        else:
            output = output + character

    return output


if __name__ == "__main__":
    key = KEY

    message = input("Enter the message to encrypt: ")

    cipher_text = vigenere_cipher(message, key, False)
    print(f"Cipher text: {cipher_text}")

    plain_text = vigenere_cipher(cipher_text, key, True)
    print(f"Plain text: {plain_text}")
