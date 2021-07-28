def abbreviate(words):
    plain = "".join(w for w in words if w.isalpha() or w.isspace() or w == "-")

    return "".join(l for l in plain.title() if l.isalpha() and l.isupper())
