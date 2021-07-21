def score(word: str):
    letter_list = list(word.lower())

    """
    letter_values ={
        ("a", "e", "i", "o", "u", "l", "n", "r", "s", "t"): 1,
        ("d", "g"): 2,
        ("b", "c", "m", "p"): 3,
        ("f", "h", "v", "w", "y"): 4,
        ("k"): 5,
        ("j", "x"): 8,
        ("q", "z"): 10
        }
    """
    
    score = 0

    for l in letter_list:
        if l in ("a", "e", "i", "o", "u", "l", "n", "r", "s", "t"):
            score += 1
        elif l in ("d", "g"):
            score += 2
        elif l in ("b", "c", "m", "p"):
            score += 3
        elif l in ("f", "h", "v", "w", "y"):
            score += 4
        elif l in ("k"):
            score += 5
        elif l in ("j", "x"):
            score += 8
        elif l in ("q", "z"):
            score += 10

    return score
