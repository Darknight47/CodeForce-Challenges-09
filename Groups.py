"""

----------------- Link for the challenge: https://codeforces.com/problemset/problem/1747/A ------------------

You are given an array a consisting of n integers. 
You want to distribute these n integers into two groups s1 and s2 (groups can be empty) so that the following conditions are satisfied:

For each i (1 ≤ i ≤ n), a(i) goes into exactly one group.
The value |sum(s1)|−|sum(s2)| is the maximum possible among all such ways to distribute the integers.
Here sum(s1) denotes the sum of the numbers in the group s1, and sum(s2) denotes the sum of the numbers in the group s2.

Determine the maximum possible value of |sum(s1)|−|sum(s2)|.

Input
The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 2⋅10^4) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 10^5) — the length of the array a.

The second line of each test case contains n integers a1,a2…an (−10^9 ≤ a(i) ≤ 10^9) — elements of the array a.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output a single integer  — the maximum possible value of |sum(s1)|−|sum(s2)|.

Input:
4
2
10 -10
4
-2 -1 11 0
3
2 3 2
5
-9 2 0 0 -4

Output:
0
8
7
11
"""


cases = int(input())
for i in range(cases):
    sze = int(input())
    lstSum = sum(list(map(int, input().split())))
    print(abs(lstSum))