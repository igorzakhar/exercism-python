def hey(phrase):
    if phrase.isupper() and phrase.endswith("?"):
        return "Calm down, I know what I'm doing!"

    if phrase.isupper():
        return "Whoa, chill out!"

    if phrase.strip().endswith("?"):
        return "Sure."

    if not phrase.strip():
        return "Fine. Be that way!"

    return "Whatever."
