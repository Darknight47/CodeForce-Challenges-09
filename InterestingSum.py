"""

---------------- Link for the challenge: https://codeforces.com/problemset/problem/1720/B ----------------------------

You are given an array a that contains n integers. You can choose any proper subsegment al,al+1,…,ar of this array, meaning you can choose any two integers 1 ≤ l ≤ r ≤ n, where r−l+1<n. 
We define the beauty of a given subsegment as the value of the following expression:

max(a1,a2,…,al−1,ar+1,ar+2,…,an)−min(a1,a2,…,al−1,ar+1,ar+2,…,an)+max(al,…,ar)−min(al,…,ar).
Please find the maximum beauty among all proper subsegments.

Input
The first line contains one integer t (1 ≤ t ≤ 1000) — the number of test cases. Then follow the descriptions of each test case.

The first line of each test case contains a single integer n (4 ≤ n ≤ 10^5) — the length of the array.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9) — the elements of the given array.
It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each testcase print a single integer — the maximum beauty of a proper subsegment.

Input:
4
8
1 2 2 3 1 5 6 1
5
1 2 3 100 200
4
3 3 3 3
6
7 8 3 1 1 8

Output:
9
297
0
14
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    arr = sorted(list(map(int, input().split())))
    diff1 = arr[sze - 1] - arr[0]
    diff2 = arr[sze - 2] - arr[1]
    print(diff1 + diff2)