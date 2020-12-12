# Part 1

## Problem: 

**What is the Manhattan distance between end location and the ship's starting position?**

## Information:

* Arbitrary Movements
    * Action N means to move north by the given value.
    * Action S means to move south by the given value.
    * Action E means to move east by the given value.
    * Action W means to move west by the given value.
* Front-facing movements
    * Action L means to turn left the given number of degrees.
    * Action R means to turn right the given number of degrees.
    * Action F means to move forward by the given value in the direction the ship is currently facing.

Manhattan distance is the sum of the absolute value of start and end points (X,Y). e.g. start at (0,0) go to (5,0), then (5,5); Manhattan distance is square root of 50 because a^2 + b^2 = c^2.


## Plan

IN: directions as {CodeNum} split up by line (string)
OUT: Manhattan distance between start and end point (float)