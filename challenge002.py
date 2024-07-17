"""
Challenge002:
https://www.reddit.com/r/dailyprogrammer/comments/pjsdx/difficult_challenge_2/
"""

import time
import os
from datetime import datetime


class StopWatch():
    """
    A stopwatch: this program should have start, stop,
    and lap options, and it should write
    out to a file to be viewed later.
    """
    __statingTime = None
    __time = None
    __lapTime = None
    __lap = None
    __started = False

    def start(self):
        """
        """
        self.__statingTime = round(time.time(), 2)
        self.__lap = self.__statingTime
        self.__started = True

    def stop(self):
        """
        """
        self.__time = round((time.time() - self.__statingTime), 2)

    def lap(self):
        """
        """
        self.__lapTime = round((time.time()  - self.__lap), 2)
        self.__lap = time.time()
        self.stop()

    def main(self):
        """
        """
        res = False
        msg01 = "~~~~~~~~~STOPWATCH~~~~~~~~~"
        msg02 = "(S)tart or (E)xit\n"
        msg03 = "(L)ap, (S)top\n"
        msg04 = "You stopwatch data are in the file "
        msg05 = "Timer{:%Y%m%dT%H%M%S}.txt".format(datetime.now())
        msg06 = "~~~~~~~~~GOODBYE~~~~~~~~~"
        file = open(msg05,"w")
        lines = []
        print(msg01)
        time.sleep(0.8)
        respStr = input(msg02)
        while(res is False):
            if (type(respStr) is not str) or\
                    (respStr.upper() not in ["S", "L", "E"]):
                print("Wrong input.\n{}".format(msg02))
            elif (respStr.upper() == "S" and self.__started == False):
                self.start()
                lines.append("StopWatch\n")
                respStr = input(msg03)
            elif (respStr.upper() == "E"):
                lines.append("Goodbye \n")
                res = True
            elif (respStr.upper() == "S" and self.__started == True):
                self.stop()
                a = "Total time : {}\n".format(self.__time)
                print(a)
                lines.append(a)
                print(msg04 + msg05)
                res = True
            elif (respStr.upper() == "L" and self.__started == True):
                self.lap()
                a = "Lap time : +{}    ,   {}\n".format(
                        self.__lapTime,
                        self.__lap - self.__statingTime
                        )
                print(a)
                lines.append(a)
                respStr = input(msg03)
            elif (self.__started == True):
                print("Wrong input.")
                print(msg03)
                res = True
            else:
                print("Wrong input.")
                print(msg02)
                res = True
        if (lines):
            file.writelines(lines)
            file.close()
        else:
            os.remove(msg05)
        print(msg06)


if __name__ == '__main__':
    StopWatch().main()
