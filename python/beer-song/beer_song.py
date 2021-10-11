from typing import List


def number(n: int) -> str:
    return 'no more' if n == 0 else str(n)

def plural(n: int) -> str:
    return '' if n == 1 else 's'

def bottles(n: int) -> str:
    return f"{number(n)} bottle{plural(n)} of beer"

def verse_1(n: int) -> str:
    return f"{bottles(n)} on the wall, {bottles(n)}.".capitalize()

def verse_2(n: int) -> str:
    if n > 0:
        return f"Take {'one' if n > 1 else 'it'} down and pass it around, {bottles(n-1)} on the wall."

    return f"Go to the store and buy some more, {bottles(99)} on the wall."

def recite(start: int, take: int = 1) -> List[str]:
    lyric = []

    while take > 0:
        lyric.append(verse_1(start))
        lyric.append(verse_2(start))

        if take > 1:
            lyric.append("")

        start -= 1
        take -= 1

    return lyric
