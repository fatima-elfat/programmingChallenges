"""
Challenge003:
https://www.reddit.com/r/dailyprogrammer/comments/pkwgf/2112012_challenge_3_difficult/
A script that takes the scrambled words below,
and compare them against the list in the file challenge003.txt to unscramble them.

The words to de-scramble:
mkeart, sleewa, edcudls, iragoge, usrlsle, nalraoci, nsdeuto, amrhat, inknsy, iferkna.
"""
def getWords(filename: str) -> dict:
    """
    """
    wordDict = {}
    file = open(filename,"r")
    for line in file.readlines():
        line = line.split("\n")[0]
        wordDict[''.join(sorted(line))] = line
    file.close()
    return wordDict

def descramble(words: list[str]) -> dict:
    """
    """
    wordDict = getWords("challenge003.txt")
    resDict = {}
    for word in words:
        w = ''.join(sorted(word))
        if wordDict[w]:
            resDict[word] = wordDict[w]
    return resDict
            
        

wordList = [ "mkeart", "sleewa", "edcudls",
            "iragoge", "usrlsle", "nalraoci",
            "nsdeuto", "amrhat", "inknsy", "iferkna"]

print(descramble(wordList))