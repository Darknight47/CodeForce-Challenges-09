"""
------------------- Link for the challenge: https://codeforces.com/problemset/problem/1932/A ------------------

During your journey through computer universes, you stumbled upon a very interesting world. It is a path with n consecutive cells, each of which can either be empty, 
contain thorns, or a coin. In one move, you can move one or two cells along the path, provided that the destination cell does not contain thorns (and belongs to the path). 
If you move to the cell with a coin, you pick it up.

You want to collect as many coins as possible. 
Find the maximum number of coins you can collect in the discovered world if you start in the leftmost cell of the path.

Input
The first line of input contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. Then the descriptions of the test cases follow.

The first line of each test case contains a single integer n (1 ≤ n ≤ 50) — the length of the path.

The second line of each test case contains a string of n characters, the description of the path. 
The character '.' denotes an empty cell, '@' denotes a cell with a coin, and '*' denotes a cell with thorns. It is guaranteed that the first cell is empty.

Output
For each test case, output a single integer, the maximum number of coins you can collect.

Input:
3
10
.@@*@.**@@
5
.@@@@
15
.@@..@***..@@@*

Output:
3
4
3
"""

cases = int(input())
for i in range(cases):
    sze = int(input())
    s = input()
    indx = 0
    coins = 0
    while(indx <= (sze - 1)):
        cell = s[indx]
        if(cell == '.' or cell == '*'):
            if(indx != (sze - 1)):
                cell2 = s[indx + 1]
                if(cell2 == '.'):
                    indx += 2
                elif(cell == '*' and cell2 == '*'):
                    break
                else:
                    indx += 1
            else:
                break
        elif(cell == '@'):
            if(indx != (sze - 1)):
                cell2 = s[indx + 1]
                if(cell2 == '@'):
                    coins += 2
                    indx += 2
                else:
                    coins += 1
                    indx += 1
            else:
                coins += 1
                indx += 1             
    print(coins)