def find_anagrams(word, candidates):
    letter_list = sorted(word.lower())

    result = [l for l in candidates if sorted(l.lower()) == letter_list and word.lower() != l.lower()]

    return result
