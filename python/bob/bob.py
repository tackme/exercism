import re

def response(hey_bob):
    plain = re.sub(r"[^a-zA-Z0-9?]", "", hey_bob)

    if not plain:
        return "Fine. Be that way!"

    if plain.isupper() and plain.endswith("?"):
        return "Calm down, I know what I'm doing!"

    if plain.isupper():
        return "Whoa, chill out!"

    if plain.endswith("?"):
        return "Sure."

    return "Whatever."
