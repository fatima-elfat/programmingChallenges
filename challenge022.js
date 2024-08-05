/*
Sorting Objects

Prompt
Given an array of objects,
sort the objects by population size. Return the entire object.

*/
const SortObj = array => {
    return array.sort((a, b) => a.population - b.population);
}

const objList = [
    { name: 'Goa', population: 9000000 },
    { name: 'Zoo', population: 870000 },
    { name: 'Wano', population: 12000000 },];
console.log(SortObj(objList));