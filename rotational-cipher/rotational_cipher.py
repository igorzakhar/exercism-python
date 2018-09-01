from string import ascii_lowercase, ascii_uppercase


def rotate(text, key):
    key %= 26

    alphabet_low = ascii_lowercase[key:] + ascii_lowercase[:key]
    alphabet_up = ascii_uppercase[key:] + ascii_uppercase[:key]

    alphabet = ascii_lowercase + ascii_uppercase
    shifted_alphabet = alphabet_low + alphabet_up
    trans_table = str.maketrans(alphabet, shifted_alphabet)

    return text.translate(trans_table)
