"""
Challenge010: Convert a decimal to a hex
For this challenge, you need to write
a function in Python that accepts a string of ASCII characters.
It should return each character’s value as a hexadecimal string.
Separate each byte by a space,
and return all alpha hexadecimal characters as lowercase.
"""


def asciiToHex(input):
    res = ""
    res = ' '.join(r'{:x}'.format(ord(c)) for c in input)
    return res


if __name__ == "__main__":
    print(asciiToHex("1234ABCDabcd"))
