/*
Two Strings Are Anagrams of Each Other

Prompt
Create a function that takes in two strings
as two parameters and returns a boolean that indicates
whether or not the first string is an anagram of the second string.

*/
const areAnagram = (input01, input02) => {
    input01 = input01.replace(" ", "").toLowerCase();
    input02 = input02.replace(" ", "").toLowerCase();
    let in01 = input01.split("").sort();
    let in02 = input02.split("").sort();
    if(in01.length != in02.length) {
        return false;
    }
    for(let i=0; i < in01.length; i++) {
        if(in01[i] != in02[i]) {
            return false;
        }
    }
    return true;
}

console.log(areAnagram("Enlist", "inlets"));
console.log(areAnagram("Enlis t", "inlets"));
console.log(areAnagram("listen", "Enlist"));
console.log(areAnagram("tinsel", "silent"));