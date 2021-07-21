def score(word: str):
    letter_list = list(word.lower())
    
    count = 0

    for l in letter_list:
        if l in ("a", "e", "i", "o", "u", "l", "n", "r", "s", "t"):
            count += 1
        elif l in ("d", "g"):
            count += 2
        elif l in ("b", "c", "m", "p"):
            count += 3
        elif l in ("f", "h", "v", "w", "y"):
            count += 4
        elif l == "k":
            count += 5
        elif l in ("j", "x"):
            count += 8
        elif l in ("q", "z"):
            count += 10

    return count
