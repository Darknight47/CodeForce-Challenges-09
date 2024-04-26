"""
Mihai has an 8×8 chessboard whose rows are numbered from 1 to 8 from top to bottom and whose columns are numbered from 1 to 8 from left to right.

Mihai has placed exactly one bishop on the chessboard. The bishop is not placed on the edges of the board. (In other words, the row and column of the bishop are between 2 and 7, inclusive.)

The bishop attacks in all directions diagonally, and there is no limit to the distance which the bishop can attack. Note that the cell on which the bishop is placed is also considered attacked.

Mihai has marked all squares the bishop attacks, but forgot where the bishop was! Help Mihai find the position of the bishop.

Input
The first line of the input contains a single integer t (1≤t≤36) — the number of test cases. The description of test cases follows. There is an empty line before each test case.

Each test case consists of 8 lines, each containing 8 characters. Each of these characters is either '#' or '.', denoting a square under attack and a square not under attack, respectively.

Output
For each test case, output two integers r and c (2≤r,c≤7) — the row and column of the bishop.

The input is generated in such a way that there is always exactly one possible location of the bishop that is not on the edge of the board.

Input:
3


.....#..
#...#...
.#.#....
..#.....
.#.#....
#...#...
.....#..
......#.


#.#.....
.#......
#.#.....
...#....
....#...
.....#..
......#.
.......#


.#.....#
..#...#.
...#.#..
....#...
...#.#..
..#...#.
.#.....#
#.......

Output:
4 3
2 2
4 5
"""
cases = int(input())
input()
input()
for i in range(cases):
    arr = []
    first = False
    x = -1
    for j in range(8):
        arr.append(input())
    for z in range(8):
        line = arr[z]
        hashtags = line.count("#")
        if(hashtags == 2 and not first):
            first = True
        elif(hashtags == 1 and first):
            x = z
            break
    temp = arr[x]
    for w in range(8):
        if(temp[w] == '#'):
            y = w
            break
    print((x + 1), (y + 1))
    if(i < (cases - 1)):
        input()
        input()