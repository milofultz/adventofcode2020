# Problem

## Rules

- 3D grid (x,y,z) with active (#) and inactive (.) states
- a 3x3x1 grid start
- During a cycle, all cubes simultaneously change their state according to the following rules:
  - If active and exactly 2 or 3 neighbors are active, it stays active. Otherwise, the cube becomes inactive. 
  - If inactive but exactly 3 neighbors are active, it becomes active. Otherwise, the cube remains inactive.
- neighbors are any of the 26 other cubes where any of their coordinates differ by at most 1. For example, given the cube at x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the cube at x=0,y=2,z=3, and so on.

## Plan (Part 1)

### Parse the data

    IN: String (lines of cubes)
    OUT: 3D array (x * y * z=1)

- Open file
- Put data split by newline into variable
- Make array containing an array containing another array for each line in the data
    - [[[letter for letter in line] for line in raw.split('\n')]]
    - Array will be 3 x 3 x 1 (X x Y x Z)
- return array

### Allow game to play for X turns

    IN: 3D array, of initial data
        int, number of turns
    OUT: 3D array of resulting data

- create deepcopy of input array as 'result'
- for each turn in X turns
    - create deepcopy of result array as 'working'
    - for each index and element in 3d array
        - get number of active neighbors(index, result)
        - if element is active AND active neighbors is less than 2 OR active neighbors is greater than 3
            - Set element to inactive in 'working' at index
        - elif element is inactive AND active neighbors is 3
            - set element to active in 'working' at index
    - expand array to fit next turn's active()
    - set 'working' array to result
- return result

### Get Number Of Active Neighbors

    IN: tuple, index of element
        3D array
    OUT: int, number of active neighbors

- set z_max to length of z axis
- set y_max to length of y axis
- set x_max to length of x axis

- if x index is 0, set x_range to "x_index:x_index+2"
- elif x index is x_max, set x_range to "x_index-1:x_index+1"
- else, set x_range to "x_index-1:x_index+2"
- if y index is 0, set y_range to "y_index:y_index+2"
- elif y index is y_max, set y_range to "y_index-1:y_index+1"
- else "y_index-1:y_index+2"
- if z index is 0, set z_range to "z_index:z_index+2"
- elif z index is z_max, set z_range to "z_index-1:z_index+1"
- else "z_index-1:z_index+2"
- make search array from input array (search_area = input[x_range, y_range, z_range])

- return number of active in search area (np.count_nonzero(condition))

### Expand array to fit next turn

    IN: 3D array
    OUT: 3D array

- Make deepcopy of input array 'working'
- for z, get max
- for y, get max
- for x, get max
- if there are any active cubes on face (0) of z axis
    - add a layer full of inactive to face of z axis on 'working'
- if there are any active cubes on back (max) of z axis
    - add a layer full of inactive to back of z axis on 'working'
- if there are any active cubes on face (0) of y axis
    - add a layer full of inactive to face of y axis on 'working'
- if there are any active cubes on back (max) of y axis
    - add a layer full of inactive to back of y axis on 'working'
- if there are any active cubes on face (0) of x axis
    - add a layer full of inactive to face of x axis on 'working'
- if there are any active cubes on back (max) of x axis
    - add a layer full of inactive to back of x axis on 'working'
- return 'working'