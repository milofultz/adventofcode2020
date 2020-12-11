## Parser

IN: Empty layout of seats (string)
OUT: Parsed seats layout

## Program

IN: Parsed seats layout
OUT: number of occupied seats (int)

Rules:
- If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
- If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
- Otherwise, the seat's state does not change.

How to store the seats layout? 
- List of lists
    - high amount of overhead needed to constantly search the lists
    - empty seats take up lots of space in list
    - easy to check adjacent seats
- hash table with coords as keys
    - fast search
    - no empty seats/less space needed
    - harder to check adjacent seats
    
Naive solution - List of lists
FUNC: Get settled seats
IN: Seat list (list of lists)
OUT: (modified copy of) Seat list (list of lists)
- make deep copy of seat list to work with
- initial state is None
- while initial state is not equal to seat list
    - initial state is deep copy of seat list
    - For row in seats
        - for each seat in row
            - if empty and can be occupied (func)
                - set to occupied
            - if occupied and can be emptied (func)
                - set to empty
- return modified copy of seat list

FUNC: Get occupied seats
IN: Seat list
OUT: Occupied seats (int)

- set counter to 0
- For row in seats
    - For seat in row
        - if seat is occupied
            - counter += 1
- return counter 