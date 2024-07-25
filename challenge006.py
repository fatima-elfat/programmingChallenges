"""
challenge006: Create a Morse code translator.
We no longer use Morse code to transfer information,
but that doesn’t mean you can’t use it in a code challenge.
Write a function in Python that takes in a string that can
have alphanumeric characters in lower or upper case.
The string can also contain any special characters handled in Morse code,
including commas, colons, apostrophes, periods,
exclamation marks, and question marks.
The function should return the Morse code equivalent for the string.
"""


class MorseCode:
    """
    Morse code translator.
    """
    __morseDict = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
        "Z": "--..", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.", "0": "-----", ", ": "--..--",
        ".": ".-.-.-", "?": "..--..", "/": "-..-.", "-": "-....-",
        "(": "-.--.", ")": "-.--.-"
    }

    def encode(self, sentence: str) -> str:
        res = ""
        if (sentence == ""):
            return res
        for c in sentence:
            if c == ' ':
                res += "  "
            res += self.__morseDict[c] + " "
        return res

    def decode(self, sentence: str) -> str:
        res = ""
        c = ""
        reverseMorse = {}
        for k, it in self.__morseDict.items():
            reverseMorse[it] = k
        if (sentence == ""):
            return res
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                if i > 0:
                    if sentence[i - 1] == ' ':
                        res += " "
                res += reverseMorse[c]
                c = ""
            elif sentence[i] not in reverseMorse.keys():
                print("the sentence is not in morse code")
                break
            else:
                c += sentence[i]
        if c != "":
            res += reverseMorse[c]
        return res

    def main(self):
        msg01 = "             Morse code translator\n"
        msg02 = "Translate:\n   (M)orse code\n  (R)eadeable test\n  (E)xit:\n"
        msg03 = "Wrong input"
        msg04 = "Enter the sentence to translate: "
        msg05 = "thank you."
        msgInput01 = ""
        msgInput01 = input(msg01 + msg02)
        while (msgInput01.upper() != "E"):
            match msgInput01.upper():
                case "M":
                    msgInput02 = input(msg04)
                    print(self.encode(msgInput02.upper()))
                    msgInput01 = input(msg02)
                case "R":
                    msgInput02 = input(msg04)
                    print(self.decode(msgInput02.upper()))
                    msgInput01 = input(msg02)
                case "E":
                    print(msg05)
                    msgInput01 = input(msg02)
                    break
                case _:
                    msgInput01 = input(msg03 + msg02)


if __name__ == '__main__':
    m = MorseCode()
    m.main()
