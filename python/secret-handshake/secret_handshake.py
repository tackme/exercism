from typing import List

def commands(binary_str: str) -> List[str]:
    handshakes = ["wink", "double blink", "close your eyes", "jump"]

    result = [handshake for index, handshake in enumerate(handshakes) if int(binary_str, 2) >> index & 1]

    if binary_str[0] == "1":
        return result[::-1]

    return result
