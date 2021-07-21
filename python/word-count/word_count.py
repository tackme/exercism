import re

def count_words(sentence):
    word_list = (re.findall("([a-zA-Z0-9]+(?:'[a-zA-Z0-9])?)", sentence.lower()))

    count = {}

    for word in word_list:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

    return count
