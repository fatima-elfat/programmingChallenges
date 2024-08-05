"""
challenge011: Find the difference between the strings.
Write a function in Python that accepts two string parameters.
The first parameter will be a string of characters,
and the second parameter will be the same string of characters,
but they’ll be in a different order and have one extra character.
The function should return that extra character.

For example, if the first parameter is “eueiieo” and the second is “iieoedue”,
then the function should return “d”.
"""


def findDiffChar(input01: str, input02: str) -> str:
    res = ""
    input01 = sorted(input01)
    input02 = sorted(input02)
    for i in input01:
        if input02:
            for j in range(len(input02)):
                if i == input02[j]:
                    del input02[j]
                    break
    if input02 != []:
        for i in input02:
            res += i
    return res


if __name__ == "__main__":
    print(findDiffChar("eueiieo", "iieoedue"))
