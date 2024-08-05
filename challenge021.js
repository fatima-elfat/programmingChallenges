/*
Armstrong Numbers

Prompt
An Armstrong number is an n-digit number that is equal to
the sum of the nth powers of its digits.
Determine if the input number is an Armstrong number.
Return either true or false.

*/
const isArmstrong = input => {
    let res = true;
    let sum = 0
    const n = ("" + input).length;
    ("" + input).split("").forEach(element => {
        sum += Math.pow(Number(element), n);
    });
    if(sum != input) {
        res = false;
    }
    return res;
}
console.log(isArmstrong(0));
console.log(isArmstrong(15));
console.log(isArmstrong(153));
console.log(isArmstrong(158));
console.log(isArmstrong(370));
console.log(isArmstrong(1634));
console.log(isArmstrong(2510));