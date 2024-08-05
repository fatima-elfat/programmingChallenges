"""
challenge014: Rearrange the number
To complete this challenge,
write a function that accepts a number as a parameter.
The function should return a number that’s
the difference between the largest and smallest
numbers that the digits can form in the number.

For example, if the parameter is “213”,
the function should return “108”,
which is the result of 123 subtracted from 321.
"""


def rearrangeNum(input):
    """
    """
    s = sorted(str(input))
    s = "".join(s[i] for i in range(len(s)-1, -1, -1))
    return int(s) - input


if __name__ == "__main__":
    print(rearrangeNum(759))
    print(rearrangeNum(213))
