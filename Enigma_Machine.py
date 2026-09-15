ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ROTOR = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
REFLECTOR = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
INITIAL_POSITION = 0

def enigma_cipher(text: str) -> str:
    position = INITIAL_POSITION
    output = ""

    for character in text:
        is_lower = character.islower()

        encrypted_character, position = encrypt_character(character.upper(), position)

        if is_lower:
            encrypted_character = encrypted_character.lower()

        output = output + encrypted_character

    return output

def encrypt_character(character: str, position: int) -> tuple[str, int]:
    alphabet = ALPHABET
    rotor = ROTOR
    reflector = REFLECTOR

    if character not in alphabet:
        return character, position

    position = rotate(position)

    input_index = (alphabet.index(character) + position) % 26
    rotor_output = rotor[input_index]
    forward_index = (alphabet.index(rotor_output) - position) % 26
    character_after_rotor = alphabet[forward_index]

    reflected_character = reflector[alphabet.index(character_after_rotor)]

    reflected_index = (alphabet.index(reflected_character) + position) % 26
    rotor_input = alphabet[reflected_index]
    reverse_index = rotor.index(rotor_input)
    final_index = (reverse_index - position) % 26
    final_character = alphabet[final_index]

    return final_character, position

def rotate(position: int) -> int:
    return (position + 1) % 26

if __name__ == "__main__":
    message = input("Enter the message to encrypt: ")

    cipher_text = enigma_cipher(message)
    print(f"Cipher text: {cipher_text}")

    plain_text = enigma_cipher(cipher_text)
    print(f"Plain text: {plain_text}")
