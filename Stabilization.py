"""

----------------- Link for the challenge: https://codeforces.com/contest/1095/problem/B ------------------------------

You are given an array a consisting of n integer numbers.

Let instability of the array be the following value: maxi=1nai−mini=1nai.

You have to remove exactly one element from this array to minimize instability of the resulting (n−1)
-elements array. Your task is to calculate the minimum possible instability.

Input
The first line of the input contains one integer n (2 ≤ n ≤ 10^5) — the number of elements in the array a.

The second line of the input contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^5) — elements of the array a.

Output
Print one integer — the minimum possible instability of the array if you have to remove exactly one element from the array a.


Input:
4
1 3 3 7

Output:
2
"""

sze = int(input())
arr = list(sorted(map(int, input().split())))
if(sze == 2):
    print(0)
else:
    diff1 = arr[sze - 1] - arr[1]
    diff2 = arr[sze - 2] - arr[0]
    print(diff1 if diff2 > diff1 else diff2)