# Problem

Given a set of bitmasks, each with a corresponding set of values, what is the sum of all values left in memory after it completes?

* IN: string containing: 
    * bitmask (string of binary overwrites and X for nothing)
    * memory location and value (string of key and of premasked value)
* OUT: int, sum of all masked values within memory when completer
* EDGE:
* CONSTRAINTS:

## Part 1

* parse data
    * open data file
    * make list of contents
    * make list to hold masks and their values [{mask: {mem: value, mem: value}]
    * set current_head to None
    * for each line in contents
        * if line starts with "mask = "
            * set mask to everything past "mask = " 
            * create new dict with key as mask and dict as value
            * set current_head to new dict
        * else, if it starts with 'mem'
            * set key to number between '[' and ']'
            * set value to number after ' = '
            * add to current_head's value dict the key:value pair
    * return list
* get sum of all masked values
  IN: dict of mask and key:values for each
  OUT: int, sum of all masked values
    * create masked values dict
    * for each new bitmask in list
        * for each memory location and value in the bitmask dict
            * convert the value to binary string
            * for each char in both the mask and the binary string:
                * if the mask char is a 0, change that binary char to a 0
                * if the mask char is an 1, change that binary char to a 1
                * else, continue
            * get int of that string
            * add that int to the memory location of the masked values dict
    * create sum of 0
    * for each key in masked values
        * add value to sum
    * return sum
        
        