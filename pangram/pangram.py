from string import ascii_lowercase


def is_pangram(sentence):
    return all([symbol in sentence.lower() for symbol in ascii_lowercase])
