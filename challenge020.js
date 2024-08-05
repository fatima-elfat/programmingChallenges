/*
Balanced Brackets

Prompt
Given a string possibly containing three types of braces ({}, [], ()),
write a function that returns a Boolean indicating
whether the given string contains a valid nesting of braces.

*/
const balencedBrackets = input => {
    let res = true
    let inp = input.replace(/[\w- ]/g, "").split("");
    const bracketDict = {
        "{": "}",
        "[":"]",
        "(": ")"
    }
    const keys = ["{", "[", "("]
    const values = ["}","]", ")"]
    let bracketList = []
    inp.forEach(element => {
        if(keys.includes(element)) {
            bracketList.push(element);
        }
        else if(values.includes(element)) {
            const a = bracketList[bracketList.length - 1]
            if(bracketDict[a] != element) {
                res = false;
            }
            else {
                bracketList.pop();
            }
        }
    });
    return res;
}

console.log(balencedBrackets("{nameLi 1f [fdf 5dfzq }st}"));
console.log(balencedBrackets("{[gheee()]}"));
console.log(balencedBrackets("{ for}"));
