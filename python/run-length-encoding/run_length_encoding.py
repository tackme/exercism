def decode(string):
    result, count = "", ""

    for letter in string:
        if letter.isdigit():
            count += letter
        elif count:
            result += letter * int(count)
            count = ""
        else:
            result += letter

    return result


def encode(string):
    if not string:
        return ""

    reslut, current, count = "", string[0], 1

    for letter in string[1:]:
        if letter == current:
            count += 1
        else:
            reslut += str(count) + current if count > 1 else current
            current = letter
            count = 1

    reslut += str(count) + current if count > 1 else current

    return reslut
