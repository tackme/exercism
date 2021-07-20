def is_isogram(string):
    converted_str = string.lower().replace(" ", "").replace("-", "")
    return len(converted_str) == len(set(converted_str))
