"""
challenge013: Tic Tac Toe blocker.
In this Python challenge,
write a function that’ll accept two numbers.
These numbers will represent a position on a tic-tac-toe board.
They can be 0 through 8, where 0 is the top-left spot,
and 8 is the bottom-right spot.

These parameters are two marks on the tic-tac-toe board.
The function should return the number of the spot
that can block these two spots from winning the game.
"""


def ticTacToe(value01, value02):
    res = 0
    winnerVal = [
        [0, 1, 2], [0, 3, 6],
        [0, 4, 8], [1, 4, 7],
        [2, 5, 8], [3, 4, 5],
        [6, 7, 8]
    ]
    for vals in winnerVal:
        if (value01 in vals) and (value02 in vals):
            res += 1
    return res


if __name__ == "__main__":
    print(ticTacToe(8, 0))
