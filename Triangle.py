"""

------------------- Link for the challenge: https://codeforces.com/problemset/problem/1398/A ---------------------

You are given an array a1,a2,…,an, which is sorted in non-decreasing order (a(i) ≤ a(i+1)).

Find three indices i, j, k such that 1≤i<j<k≤n and it is impossible to construct a non-degenerate triangle 
(a triangle with nonzero area) having sides equal to ai, aj and ak (for example it is possible to construct a non-degenerate triangle with sides 3, 4 and 5 but impossible with sides 3, 4 and 7). 
If it is impossible to find such triple, report it.

Input
The first line contains one integer t (1 ≤ t ≤ 1000) — the number of test cases.

The first line of each test case contains one integer n (3 ≤ n ≤ 5⋅10^4) — the length of the array a.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9; a(i−1) ≤ a(i)) — the array a.

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each test case print the answer to it in one line.

If there is a triple of indices i, j, k (i<j<k) such that it is impossible to construct a non-degenerate triangle having sides equal to ai, aj and ak, print that three indices in ascending order.
If there are multiple answers, print any of them.

Otherwise, print -1.

Input:
3
7
4 6 11 11 15 18 20
4
10 10 10 11
3
1 1 1000000000

Output:
2 3 6
-1
1 2 3
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = list(map(int, input().split()))
    first = lst[0]
    second = lst[1]
    third = lst[sze - 1]
    sum1 = first + second
    sum2 = first + third
    sum3 = second + third
    if(sum1 > third and sum2 > second and sum3 > first):
        print(-1)
    else:
        print(1, 2, sze)
