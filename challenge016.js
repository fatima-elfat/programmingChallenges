/*
Longest String in an Array
Prompt
Write a function that accepts an array of strings.
Return the longest string.

*/
const longestStr = array => {
    let res = "";
    array.forEach(element => {
        if(res.length < element.length) {
            res = element;
        }
    });
    return res;
}

const nameList = ["John", "Mike", "Danny", "Lisa", "Sophie"];
console.log(longestStr(nameList));