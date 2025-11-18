UPPER = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
LOWER = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ABC_LEN = len(UPPER)


def _shift_char(ch, shift, encrypt=True):
    if ch in UPPER:
        alphabet = UPPER
    elif ch in LOWER:
        alphabet = LOWER
    else:
        return ch

    idx = alphabet.index(ch)
    if not encrypt:
        shift = -shift
    new_idx = (idx + shift) % ABC_LEN
    return alphabet[new_idx]


def decrypt_growing_shift(ciphertext, start=1, delta=1):
    plaintext = ""
    shift = start
    for ch in ciphertext:
        if ch.isalpha():
            plaintext += _shift_char(ch, shift, encrypt=False)
            if ch in UPPER or ch in LOWER:
                shift += delta
        else:
            plaintext += ch
    return plaintext


def encrypt_growing_shift(plaintext, start=1, delta=1):
    ciphertext = ""
    shift = start
    for ch in plaintext:
        if ch.isalpha():
            ciphertext += _shift_char(ch, shift, encrypt=True)
            if ch in UPPER or ch in LOWER:
                shift += delta
        else:
            ciphertext += ch
    return ciphertext
