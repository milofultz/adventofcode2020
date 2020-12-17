## Problem

Determine if each ticket is valid. Sum each value that is not valid in each ticket. Return that sum.

## Rules

Fields each have valid ranges of values. 

    class: 1-3 or 5-7

One of the fields in every ticket is named class and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3 and 5 are both valid in this field, but 4 is not).

Ticket is CSV, all are the same 

## Plan

### Parse Data

- Get your ticket and other ticket data by looking from the end for header
  - list of lists, list holding a list containing each value
- Get fields by looking from top until 2 consecutive newlines
  - split by ": ", get header and value range
  - split value range into tuple of (low, high)
