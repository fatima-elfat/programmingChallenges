"""
Challenge004:
https://www.reddit.com/r/dailyprogrammer/comments/pm7g7/2122012_challange_4_difficult/
"""
import itertools
 


def numbersRel(numbers: list[int]) -> list[str]:
    """Takes a series of numbers (5, 3, 15)
    and find how those numbers can add, subtract,
    multiply, or divide in various ways to relate to eachother.

    Args:
        numbers (list[int]): list of numbers.

    Returns:
        list[str]: the list of possible operations.
    """
    lenL = len(numbers)
    res = ""
    nbrs = list(itertools.permutations(numbers))
    for i in range(len(nbrs)):
        if((nbrs[i][0] + nbrs[i][1]) == nbrs[i][2]):
            res += "{} + {} = {}\n".format(nbrs[i][0], nbrs[i][1], nbrs[i][2])
        if((nbrs[i][0] - nbrs[i][1]) == nbrs[i][2]):
            res += "{} - {} = {}\n".format(nbrs[i][0], nbrs[i][1], nbrs[i][2])
        if((nbrs[i][0] * nbrs[i][1]) == nbrs[i][2]):
            res += "{} * {} = {}\n".format(nbrs[i][0], nbrs[i][1], nbrs[i][2])
        if((nbrs[i][1]  and (nbrs[i][0] / nbrs[i][1])) == nbrs[i][2]):
            res += "{} / {} = {}\n".format(nbrs[i][0], nbrs[i][1], nbrs[i][2])
    return res

def getList(numbers: str) -> list[int]:
    """
    """
    lenL = len(numbers)
    res = []
    for i in range(lenL):
        res.append([int(i) for i in numbers[i].split(',')])
    return res
        

numbersList = ["5, 3, 15", "4, 2, 8", "6, 2, 12", "6, 2, 3",
               "9, 12, 108", "4, 16, 64", "2, 4, 6"]

a = getList(numbersList)
for i in range(len(a)):
    print("Combination for {}:".format(numbersList[i]))
    print(numbersRel(a[i]))