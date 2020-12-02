const findButton = document.getElementById('find-button');
findButton.addEventListener('click', addSumsOfGivenNumsToPage);

function addSumsOfGivenNumsToPage() {
  const givenNums = document
    .getElementById('data')
    .value.split('\n')
    .map((num) => parseInt(num));
  const [twoAnswer, threeAnswer] = findProductOfNumbersThatSumTo2020(givenNums);
  const answersSpan = document.getElementById('answers');
  answersSpan.innerText =
    `Two Numbers Solution: ${twoAnswer}\n` +
    `Three Numbers Solution: ${threeAnswer}`;
}

function findProductOfNumbersThatSumTo2020(numbers) {
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
