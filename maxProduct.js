function adjacentElementsProduct(array) {
  let result = [];

  for (let i = 0; i < array.length - 1; i++) {
    result.push(array[i] * array[i+1])
  }
  let maxNum = result[0];
  for (let i = 0; i < result.length; i++) {
    if (result[i] > maxNum) {
       maxNum = result[i];
    }
  }
  return maxNum;
}
