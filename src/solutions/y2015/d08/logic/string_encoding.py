def memory_length(code: str) -> int:
    """Return the number of in-memory characters for a string literal.

    The code string must include the surrounding double-quote characters.
    Recognised escape sequences: \\\\ , \\" , \\xNN.
    """
    # strip surrounding quotes
    inner = code[1:-1]
    count = 0
    i = 0
    while i < len(inner):
        if inner[i] == "\\" and i + 1 < len(inner):
            next_char = inner[i + 1]
            if next_char in {"\\", '"'}:
                count += 1
                i += 2
            elif next_char == "x":
                count += 1
                i += 4  # \xNN
            else:
                count += 1
                i += 2
        else:
            count += 1
            i += 1
    return count


def encoded_length(code: str) -> int:
    """Return the length of the re-encoded string literal for the given code.

    Each backslash and double-quote in the original code becomes two characters
    in the encoding, and the whole thing is wrapped in a new pair of quotes.
    """
    extra = sum(1 for ch in code if ch in {"\\", '"'})
    return len(code) + extra + 2
