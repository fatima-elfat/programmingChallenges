"""
challenge015: Duplicate letter checker.
Create a function in Python that accepts one parameter:
a string that’s a sentence. This function should return
True if any word in that sentence contains duplicate letters and False if not.
"""


def duplicateLetter(input):
    """
    """
    r = ""
    s = sorted(input)
    x = lambda a: a[1:]
    print(s)
    while s:
        if r == s[0] and r != " ":
            return True
        r = s[0]
        s = x(s)
    return False


if __name__ == "__main__":
    print(duplicateLetter("that sentence contains duplicate"))
    print(duplicateLetter(" contais "))
