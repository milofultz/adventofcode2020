08
---

- input: list of ints
- output: int
- constraints: 
- edge:

- get data (parse to list)
- find first number that does not follow the convention
    - get previous 25 numbers into components list (start at 1st-25th)
    - get current number (start at 26th number)
    - test if current number is sum of component numbers 
    {
        - for each number in components list
            - for each number between the next and the last
                - add the two
                - if the two add up to current number
                    - return True
            - (if none do) return False
    }
    - if so, continue
    - if not, return number