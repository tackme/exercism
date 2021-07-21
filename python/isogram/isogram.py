import re

def is_isogram(string):
    converted_str = re.sub("[ -]", "", string.lower())
    return len(converted_str) == len(set(converted_str))
