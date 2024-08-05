/*
Most Commonly Used Character in String

Prompt
Write a function that takes a string,
and returns the character that is most commonly used in the string.

*/
const mostUsedChar = input => {
    var dictChar = {}
    let maxChar = "";
    let maxIter = 0;
    let i = 0;
    for(i=0; i < input.length; i++) {
        dictChar[input[i]] = ++dictChar[input[i]] || 1
    }
    Object.entries(dictChar).forEach(([key, val]) => {
        if (maxIter < val) {
            maxIter =  val
            maxChar = key
        }
    })
    return maxChar;
}

const nameList = ["Soloman", "Fatima zahra", "Danny", "Lissa"];
nameList.forEach(element => {
    console.log(element, mostUsedChar(element));
});
