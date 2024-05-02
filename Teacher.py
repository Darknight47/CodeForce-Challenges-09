"""

---------------- Link for the challenge: https://codeforces.com/problemset/problem/1855/A --------------------

Dalton is the teacher of a class with n students, numbered from 1 to n. 
The classroom contains n chairs, also numbered from 1 to n. Initially student i is seated on chair p(i). 
It is guaranteed that p1,p2,…,pn is a permutation of length n.

A student is happy if his/her number is different from the number of his/her chair. In order to make all of his students happy, 
Dalton can repeatedly perform the following operation: choose two distinct students and swap their chairs. What is the minimum number 
of moves required to make all the students happy? One can show that, under the constraints of this problem, it is possible to make all the students happy with a finite number of moves.

A permutation of length n is an array consisting of n distinct integers from 1 to n in arbitrary order. For example, [2,3,1,5,4] is a permutation, 
but [1,2,2] is not a permutation (2 appears twice in the array), and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 1000). 
The description of the test cases follows.

The first line contains a single integer n (2 ≤ n ≤ 10^5) — the number of students.

The second line contains n integers p1,p2,…,pn (1 ≤ p(i) ≤ n) — p(i) denotes the initial chair of student i. 
It is guaranteed that p is a permutation.

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each test case, output the minimum number of moves required.

Input:
5
2
2 1
3
1 2 3
5
1 2 5 4 3
4
1 2 4 3
10
10 2 1 3 6 5 4 7 9 8

Output:
0
2
2
1
1
"""

import math
cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = list(map(int, input().split()))
    posIndx = 1
    needChange = 0
    ans = 0
    for j in range(sze):
        temp = lst[j]
        if(temp == posIndx):
            needChange += 1
        posIndx += 1
    ans = math.ceil(needChange / 2)
    print(ans)