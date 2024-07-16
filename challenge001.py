
"""
Challenge001:
https://www.reddit.com/r/dailyprogrammer/comments/pii6j/difficult_challenge_1/

"""
import random
import time


class GuessingGame():
    """
    We all know the classic "guessing game" with higher or lower prompts.
    The program  will guess numbers between 1-100,
    and respond appropriately based on whether users
    say that the number is too high or too low.
    Try to make a program that can guess the users number.
    """
    __min = 0
    __max = 100

    def randomNumber(self):
        """
        Return a random number from min to max.
        """
        return (random.randint(self.__min, self.__max))

    def game(self):
        """
        """
        res = False
        msg01 = "(Y)es, (L)ower or (H)igher. (E)xit."
        msg02 = "Thank you for playing the game. SEE YA."
        msg03 = "Yes I win!!!!!"
        print("      ------------Welcome to Guessing Game------------")
        time.sleep(0.8)
        print("--------------Choose a number from 0 to 100.--------------")
        time.sleep(2)
        print("-----------------Let the guessing begin-----------------")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        while(res is False):
            a = self.randomNumber()
            print("Is the number you choose {:d}?".format(a))
            time.sleep(0.8)
            respStr = input(msg01)
            if (type(respStr) is not str) or\
                    (respStr.upper() not in ["Y", "L", "H", "E"]):
                raise TypeError("Wrong input.\n{}".format(msg01))
            if (respStr.upper() == "E"):
                res = True
                print(msg02)
            elif (respStr.upper() == "Y"):
                res = True
                print(msg03)
            elif (respStr.upper() == "L"):
                self.__max = a
            elif (respStr.upper() == "H"):
                self.__min = a
            if (self.__min == 100 or self.__max == 1):
                print("this is cheating the number shoud be betwwen 1 and 100")
                res = True


if __name__ == '__main__':
    GuessingGame().game()
