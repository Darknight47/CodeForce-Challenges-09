"""

---------------- Link for the challenge: https://codeforces.com/problemset/problem/1972/A --------------------------

A contest contains n problems and the difficulty of the i-th problem is expected to be at most bi. There are already n problem proposals and the difficulty of the i-th problem is a(i). 
Initially, both a1,a2,…,an and b1,b2,…,bn are sorted in non-decreasing order.

Some of the problems may be more difficult than expected, so the writers must propose more problems. When a new problem with difficulty w
 is proposed, the most difficult problem will be deleted from the contest, and the problems will be sorted in a way that the difficulties are non decreasing.

In other words, in each operation, you choose an integer w, insert it into the array a, sort array a in non-decreasing order, and remove the last element from it.

Find the minimum number of new problems to make ai≤bi for all i.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). The description of the test cases follows.

The first line of each test case contains only one positive integer n (1 ≤ n ≤ 100), representing the number of problems.

The second line of each test case contains an array a of length n (1 ≤ a1 ≤ a2 ≤ ⋯ ≤ an ≤ 10^9).

The third line of each test case contains an array b of length n (1 ≤ b1 ≤ b2 ≤ ⋯ ≤ bn ≤ 10^9).

Output: For each test case, print an integer as your answer in a new line.

Example Input:
2
6
1000 1400 2000 2000 2200 2700
800 1200 1500 1800 2200 3000
6
4 5 6 7 8 9
1 2 3 4 5 6

Output:
2
3
"""

cases = int(input())
for i in range(cases):
    sze = int(input())
    aarr = list(map(int, input().split()))
    barr = list(map(int, input().split()))
    tempIndx = 0
    for i in range(sze):
        btemp = barr[i]
        atemp = aarr[tempIndx]
        if btemp >= atemp:
            tempIndx += 1
    print(sze - tempIndx)