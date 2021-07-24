import re

def count_words(sentence):
    word_list = (re.findall("([a-z0-9]+(?:'[a-z0-9])?)", sentence.lower()))

    count = {word: word_list.count(word) for word in word_list}

    return count
