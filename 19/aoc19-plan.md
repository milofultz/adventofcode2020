# Part 1: Problem

Determine the number of messages that completely match rule 0.

* IN:  Rules and messages (str)
* OUT: Number of valid messages (int)

## Rules

### For the "rules"

* Some rules, like 3: "b", simply match a single character (in this case, b).
* The remaining rules list the sub-rules that must be followed.
* A pipe `|` means that at least one of the sub-rules separated by the pipe must match.
* A rule will create strings eventually based upon the single letters found at the "base" of the nested rules.

### For the "messages"

* Valid messages should obey the rules.

## Plan

### Parse Data

IN:  String
OUT: Dict, rules
     List, messages

* Load file
* Split up messages and rules
* Create dict for rules
* For each rule
    * Split at ': '
    * If there are quotes in the suffix
        * Add number: letter (no quotes) to dict
    * set prefix to number
    * set suffix to raw rule
    * create rule list
    * If raw rule contains a pipe
        * split at ' | '
        * push both rules to rule list
    * else, push raw rule to rule list
    * Add number: rule list to dict
* Set messages to list split at newlines

### Get all the possible valid rule outputs

IN:  Dict, rules
OUT: set, valid options

* Make a new dict for seen rules
* Create a new set for valid rule outputs
* For each numbered rule in rules dict
    * Add that number to the seen rules set
    * get outputs of rule to valid outputs set
    * add outputs to valid set
    * set seen dict {number: set(outputs)}
* return valid set

#### Get valid outputs of rule group

IN:  numbered rule, list (of lists)
     rules, dict
OUT: valid, set

* create valid set
* for rule group in group
    * create output array with empty string inside
    * for rule in rule group
        * if rule is "a" or "b"
            * make output array = element + ("a" or "b") for each element in output
        * else
            * set result to func(rules[rule])
            * create temporary array
            * for element in output array
                * for addition in result
                    * add element + addition to temporary array
    * add all of output array to valid set
* return valid set

### Check each message for validity and return number of valid messages

IN:  valid outputs, set
     messages, list
OUT: number of valid messages, int

* create total = 0
* for each message in messages
    * total += 1 if message in valid set else 0
* return total

# Part 2: Problem

When changing the rules, we have added infinite loops. If you have these additional loops, how may valid messages are there?

## Plan:

First thought is to just create special cases for these changes.

    8: 42 | 42 8
    11: 42 31 | 42 11 31

So looking at this totally isolated, we could change the way this is written. FOr 8:

    8: 42 | 42 8

Which is technically the same as

    8: 42 | 42 (42)

Which can reduce down to 

    8: 42*x

Meaning that wherever 8 is, we could reliably just replace the 8's with X amount of 42's, based upon total length necessary. Similarly for 11:

    11: 42 31 | 42 11 31
    11: 42 31 | 42 (42 31) 31
    11: 42*x 31*x

Where the same amount of 42's show up as 31's.

So we can check to see if the rule contains its own number. At the beginning, if we get the length of the longest possible message, we can just return X amount until the length exceeds that maximum.

Because this is recursive, I think we would need to ensure that we don't repeat this exact scenario over and over, so there should be a separate function that will gather enough of the outputs of the recursive rule until it exceeds the max length, and then return it and add it, just like you would normally.