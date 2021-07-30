def is_pangram(sentence):
    plain = "".join(c.lower() for c in sentence if c.isalpha())

    return len(set(plain)) == 26
