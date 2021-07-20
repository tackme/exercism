import re

def is_isogram(string):
    lower_str = string.lower()
    converted_str = re.sub("[ -]", "", lower_str)
    return len(converted_str) == len(set(converted_str))
