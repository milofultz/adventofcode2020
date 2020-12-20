# Part 2 Problem

Figure out how many different ways they can be arranged. 

## Rules:

Any adapter can take an input 1, 2, or 3 jolts lower than its rating.

Treat the charging outlet near your seat as having an effective joltage rating of 0.

Your device has a built-in joltage adapter rated for 3 jolts higher than the highest-rated adapter in your bag.

Every arrangement needs to connect the charging outlet to your device.

(Implied: you don't need to use every adapter in each permutation)

## Plan

### Parse Data

### Get amount of permutations of adapters

    IN: list, adapters
    OUT: int, number of variations

- set total to 0
-- base case
- if length of adapter array is 1, return 1
-- recursive case
- else:
    - first array element is start
    - for each index, adapter in list:
        - if adapter is less than or equal to 3 over the first adapter in the array
            - sum += func([start] + array[index:])
- return sum
