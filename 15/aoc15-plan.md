# Problem

Given your starting numbers, what will be the 2020th number spoken?

Puzzle input: 19,0,5,1,10,13

## Rules

Each turn consists of considering the most recently spoken number:

- If first time seeing the number: return 0.
- Else, return the difference between the turn number when it was last spoken and the turn number of the time it was most recently spoken before then. (If spoked on turn 1 and then again on turn 3, the next number will be 3 - 1 = 2)

## Plan

- Parse the data. 
  IN: string of starting numbers separated by commas
  OUT: list of starting numbers
  - return the integer version of each char separated by commas
- Get the value of what number will be spoken on the 2020th turn. Make a function that takes in the starting numbers and a turn number as input
  IN: list of starting ints
      int, turn number to get value of
  OUT: int, value considered on provided turn number
    - define a dict that holds keys (number) and value dict {later_turn: last seen, earlier_turn: -1}
    - for turn and number in starting numbers
          - set current number to starting number list at index "turn counter"
          - create dict key of current number with value as {later_turn: turn, earlier_turn: -1}
    - define previous number as last number in starting numbers list 
    - Define the turn counter at length of starting numbers list
    - while turn counter is less than end turn number
        - if previous number is not in dict:
          - create dict key of current number with value as {later_turn: turn_counter, earlier_turn: -1}
          - set previous number to 0
        - else:
          - set current_number to later_turn - last turn
          - set dict value of current number to {later_turn: turn_counter, earlier_turn: later_turn}  
          - set previous number to current_number
    - return previous number
