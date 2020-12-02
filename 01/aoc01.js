import givenNums from '/aoc01-data.js';

function findTwoNumbersThatSumTo2020(numbers) {
  let output = '';
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i; j < numbers.length; j++) {
      output =
        numbers[i] + numbers[j] === 2020 ? numbers[i] * numbers[j] : output;
    }
  }
  return output;
}

function findThreeNumbersThatSumTo2020(numbers) {
  let output = '';
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i; j < numbers.length; j++) {
      for (let k = j; k < numbers.length; k++) {
        output =
          numbers[i] + numbers[j] + numbers[k] === 2020
            ? numbers[i] * numbers[j] * numbers[k]
            : output;
      }
    }
  }
  return output;
}

console.log('Two Numbers Solution: ' + findTwoNumbersThatSumTo2020(givenNums));
console.log(
  'Three Numbers Solution: ' + findThreeNumbersThatSumTo2020(givenNums)
);
