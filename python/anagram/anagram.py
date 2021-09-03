def find_anagrams(word, candidates):
    letter_list = sorted(word.lower())

    result = []

    for candidate in candidates:
        if sorted(candidate.lower()) == letter_list and word.lower() != candidate.lower():
            result.append(candidate)

    return result
