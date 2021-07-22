import re

def abbreviate(words):
    word_l = re.findall("([a-zA-Z0-9]+(?:'[a-zA-Z0-9])?)", words.title())

    result = ""

    for word in word_l:
        result += word[0]

    return result
