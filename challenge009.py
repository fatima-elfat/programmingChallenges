"""
Challenge009: Parse an encoded string.
In this Python challenge, you need to write a function that accepts
an encoded string as a parameter.
This string will contain a first name, last name, and an id.

Values in the string can be separated by any number of zeros.
The id is a numeric value but will contain no zeros.
The function should parse the string and return
a Python dictionary that contains the first name, last name, and id values.

An example input would be “Robert000Smith000123”.
The function should return the following using that input:
{ “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }
"""


def encodeStr(input):
    res = {
        "first_name": "",
        "last_name": "",
        "id": "",
    }
    k = iter([i for i in res.keys()])
    word = ""
    for c in input:
        if c != '0':
            word += c
        elif c == '0' and word != "":
            res[next(k)] = word
            word = ""
    if word != "":
        res[next(k)] = word
    return res


if __name__ == "__main__":
    print(encodeStr("Robert00000Smith00012300"))
    print(encodeStr("0000Robert000Smith00012300"))
    print(encodeStr("Robert000Smith000123"))
    print(encodeStr("Robert00000Smith0123"))
