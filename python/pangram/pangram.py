def is_pangram(sentence):
    sentence = "".join(c.lower() for c in sentence if c.isalpha())

    return len(set(sentence)) == 26
