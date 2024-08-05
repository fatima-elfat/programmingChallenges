"""
challenge012: Shadow sentences.
For the purpose of this challenge, shadow sentences are sentences
where every word is the same length and order
but without any of the same letters.
Write a function that accepts two parameters that may or
may not be shadows of each other. The function should return
True if they are and False if they aren’t.

An example would be “they are round” and “fold two times,”
which are shadow sentences, while “his friends”
and “our company” are not because both contain an n.
"""


def findSameChar(input01: str, input02: str) -> str:
    res = ""
    input01 = sorted(input01)
    input02 = sorted(input02)
    for i in input01:
        for j in range(len(input02)):
            if i == input02[j]:
                res += i
    return res


def areShadow(sentence01, sentence02):
    s01 = sentence01.split(" ")
    s02 = sentence02.split(" ")
    if len(s01) != len(s02):
        return False
    for i in range(len(s01)):
        if len(s01[i]) != len(s02[i]):
            return False
        same = findSameChar(s01[i], s02[i])
        if same != "":
            return False
    return True


if __name__ == "__main__":
    print(areShadow("they are round", "fold two times"))
    print(areShadow("his friends", "our company"))
