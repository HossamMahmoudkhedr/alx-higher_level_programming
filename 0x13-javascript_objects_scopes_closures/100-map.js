#!/usr/bin/node
const list = require('./100-data').list;
let newList = list.map((el, index) => el * index);

console.log(list);
console.log(newList);
