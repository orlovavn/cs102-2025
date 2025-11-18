import random
import typing as tp


def is_prime(n: int) -> bool:
    """Проверка простоты числа."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """Алгоритм Евклида для НОД."""
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(e: int, phi: int) -> int:
    """Расширенный алгоритм Евклида для обратного по модулю."""
    old_r, r = phi, e
    old_s, s = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s

    if old_s < 0:
        old_s += phi
    return old_s


def generate_keypair(p: int, q: int) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    if p == q:
        raise ValueError("p and q cannot be equal")

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = multiplicative_inverse(e, phi)
    return (e, n), (d, n)


def encrypt(pk: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    key, n = pk
    return [(ord(char) ** key) % n for char in plaintext]


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    key, n = pk
    return "".join(chr((char ** key) % n) for char in ciphertext)


if __name__ == "__main__":
    print("RSA Encrypter/Decrypter")

    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (not the one you entered above): "))

    print("Generating your public/private keypairs now...")
    public, private = generate_keypair(p, q)
    print("Your public key is", public, "and your private key is", private)

    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)

    print("Your encrypted message is:")
    print(" ".join(map(str, encrypted_msg)))

    print("Decrypting message with public key", public, "...")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))