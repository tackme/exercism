import re

def response(hey_bob):
    plain = re.sub(r"[^a-zA-Z0-9?]", "", hey_bob)

    if not plain:
        return "Fine. Be that way!"
    elif plain.isupper() and plain.endswith("?"):
        return "Calm down, I know what I'm doing!"
    elif plain.isupper():
        return "Whoa, chill out!"
    elif plain.endswith("?"):
        return "Sure."
    else:
        return "Whatever."
