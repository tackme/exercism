import string

def rotate(text, key):
    plain = string.ascii_lowercase
    cipher = plain[key:] + plain[:key]

    trans = str.maketrans(plain + plain.upper(), cipher + cipher.upper())

    return text.translate(trans)
