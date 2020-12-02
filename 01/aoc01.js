import givenNums from '/aoc01-data.js';

function findNumbersThatSumTo2020(numbers) {
  let twoAnswer, threeAnswer;
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i; j < numbers.length; j++) {
      if (numbers[i] + numbers[j] === 2020) {
        twoAnswer = numbers[i] * numbers[j];
      }
      for (let k = j; k < numbers.length; k++) {
        if (numbers[i] + numbers[j] + numbers[k] === 2020) {
          threeAnswer = numbers[i] * numbers[j] * numbers[k];
        }
      }
    }
  }
  return [twoAnswer, threeAnswer];
}

const [twoAnswer, threeAnswer] = findNumbersThatSumTo2020(givenNums);
console.log(
  `Two Numbers Solution: ${twoAnswer}\n` +
    `Three Numbers Solution: ${threeAnswer}`
);
