'use strict';

const caseSolve = function (arg) {
  let Upper = [];
  let Lower = [];
  const newArg = arg.split('');

  for (let i = 0; i < newArg.length; i++) {
    // Comparing lowercase/Uppercase to all upercase
    if (newArg[i] === newArg[i].toUpperCase()) {
      Upper.push(newArg[i]);
    } else {
      Lower.push(newArg[i]);
    }
  }
  if (Upper.length === Lower.length) {
    return arg.toLowerCase();
  } else if (Upper.length > Lower.length) {
    return arg.toUpperCase();
  } else {
    return arg.toLowerCase();
  }
}

console.log(caseSolve('code'));
console.log(caseSolve('CODe'));
console.log(caseSolve('COde'));
console.log(caseSolve('Code'));
