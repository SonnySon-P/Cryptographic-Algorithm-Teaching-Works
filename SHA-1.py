H = [
    0x67452301,
    0xEFCDAB89,
    0x98BADCFE,
    0x10325476,
    0xC3D2E1F0
]

K = [
    0x5A827999,
    0x6ED9EBA1,
    0x8F1BBCDC,
    0xCA62C1D6
]

def sha1(data: str) -> str:
    if isinstance(data, str):
        data = data.encode("utf-8")

    original_bit_length = len(data) * 8

    data = data + b"\x80"
    
    while (len(data) * 8) % 512 != 448:
        data = data + b"\x00"

    data = data + original_bit_length.to_bytes(8, byteorder = "big")

    h0, h1, h2, h3, h4 = H

    for chunk_start in range(0, len(data), 64):
        chunk = data[chunk_start : chunk_start + 64]

        W = []

        for i in range(16):
            W.append(int.from_bytes(chunk[i * 4 : i * 4 + 4], byteorder = "big"))

        for i in range(16, 80):
            W.append(left_rotate(W[i - 3] ^ W[i - 8] ^ W[i - 14] ^ W[i - 16], 1))

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for i in range(80):
            if i <= 19:
                f = (b & c) | ((~b) & d)
                k = K[0]

            elif i <= 39:
                f = b ^ c ^ d
                k = K[1]

            elif i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = K[2]

            else:
                f = b ^ c ^ d
                k = K[3]

            temporary = (left_rotate(a, 5) + f + e + k + W[i]) & 0xffffffff

            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temporary

        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff

    return f"{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}"

def left_rotate(x: int, n: int) -> int:
    return ((x << n) | (x >> (32 - n))) & 0xffffffff

if __name__ == "__main__":

    message = input("Enter the message to SHA-1: ")

    result = sha1(message)

    print(f"SHA-1: {result}")
