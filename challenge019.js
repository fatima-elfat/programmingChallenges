/*
String Permutation is Palindrome?

Prompt
Given a string, write a function
that will return whether or not that string is a palindrome.

*/
const isPlindrome = input => {
    let inp = input.toLowerCase().split("");
    let middle  = 0;
    const maxI = inp.length;
    var i, j;
    if((maxI % 2) == 0) {
        middle = maxI / 2;
    }
    else {
        middle = maxI / 2 + 1;
    }
    for(i=0, j=maxI - 1; i < middle, j >= middle; i++, j--) {
        if(inp[i] != inp[j]) {
            return false;
        }
    }
    return true;
}

console.log(isPlindrome("non"));
console.log(isPlindrome("level"));
console.log(isPlindrome("speadhaeps"));
console.log(isPlindrome("kinnikinnik"));
