def abbreviate(words):
    plain = "".join(w for w in words if w.isalpha() or w.isspace() or w == "-")

    return "".join(l[0].upper() for l in plain.replace("-", " ").split())
