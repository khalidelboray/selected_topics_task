# Caesar Cipher algorith implementation
import numpy as np


def Caesar_Cipher(
    text: str, shift: int, maintain_case: bool, ignore_forigin: bool
) -> str:
    """[summary]

    Args:
        text (str): [description]
        shift (int): [description]
        maintain_case (bool): [description]
        ignore_forigin (bool): [description]

    Returns:
        str: [description]
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for letter in text:
        if letter in alphabet or letter.lower() in alphabet:
            char = alphabet[(alphabet.index(letter.lower()) + shift) % 26]
            if maintain_case and letter.isupper():
                result += char.upper()
            else:
                result += char
        elif not ignore_forigin:
            result += letter
    return result


# Transpotition Cipher algorith implementation using numpy matrix
def Transposition_Cipher(text: str, key: str) -> str:
    """[summary]

    Args:
        text (str): [description]
        key (str): [description]

    Returns:
        str: [description]
    """
    key_str = key
    key = len(key)
    ciphermatrix = np.matrix(data=[[""] * key] * key, dtype=str)
    text_nda = np.array(list(text))

    for i in range(key):
        row = text_nda[key * i : key * (i + 1)]
        if len(row) < key:
            row = np.append(row, np.array([""] * (key - len(row))))
        ciphermatrix[i] = row

    ciphertext = ""
    shifted_indexes = sorted(
        dict(enumerate(key_str)), key=lambda x: dict(enumerate(key_str))[x]
    )
    for i in shifted_indexes:
        ciphertext += "".join(ciphermatrix[:, i].reshape(1, key).tolist()[0])
    return ciphertext


if __name__ == "__main__":
    print(Caesar_Cipher("Hello World!", 3, True, False))
    print(Transposition_Cipher("Hello World", "test"))
