from math import gcd
import random

PRIME_BITS = 20
PUBLIC_EXPONENT = 65537

def generate_keypair() -> tuple[tuple[int, int], tuple[int, int]]:
    e = PUBLIC_EXPONENT

    while True:
        p, q = generate_prime_pair()

        n = p * q
        phi_n = (p - 1) * (q - 1)

        if gcd(e, phi_n) == 1:
            break

    d = modular_inverse(e, phi_n)

    return (e, n), (d, n)

def generate_prime_pair() -> tuple[int, int]:
    p = generate_prime()

    while True:
        q = generate_prime()
        if q != p:
            return p, q

def generate_prime() -> int:
    bits = PRIME_BITS
    
    while True:
        n = random.getrandbits(bits)

        n = n | (1 << (bits - 1))
        n = n | 1

        if is_prime(n):
            return n

def is_prime(n: int) -> bool:
    if n < 2:
        return False

    if n == 2:
        return True
    
    if n % 2 == 0:
         return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

def modular_inverse(a: int, m: int) -> int:
    return pow(a, -1, m)

def encrypt(message: int, public_key: int) -> int:
    e, n = public_key

    if not (0 <= message < n):
        raise ValueError("The message is too long to be encrypted.")

    return pow(message, e, n)

def decrypt(cipher_text: int, private_key: int) -> int:
    d, n = private_key

    return pow(cipher_text, d, n)

if __name__ == "__main__":
    public_key, private_key = generate_keypair()

    print("Public key:", public_key)
    print("Private key:", private_key)

    message = input("Enter the message to encrypt: ")
    message_bytes = message.encode("utf-8")
    message_int = int.from_bytes(message_bytes, byteorder = "big")
    cipher_text = encrypt(message_int, public_key)
    print(f"Cipher text: {cipher_text}")

    plain_text_int = decrypt(cipher_text, private_key)
    plain_text_bytes = plain_text_int.to_bytes((plain_text_int.bit_length() + 7) // 8, byteorder = "big")
    plain_text = plain_text_bytes.decode("utf-8")
    print(f"Plain text: {plain_text}")