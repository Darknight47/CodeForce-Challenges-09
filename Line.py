"""

----------------- Link for the challenge: https://codeforces.com/problemset/problem/1837/A --------------------------

You are given two integers x and k. Grasshopper starts in a point 0 on an OX axis. In one move, it can jump some integer distance, that is not divisible by k, to the left or to the right.

What's the smallest number of moves it takes the grasshopper to reach point x? What are these moves? If there are multiple answers, print any of them.

Input
The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of testcases.

The only line of each testcase contains two integers x and k (1 ≤ x ≤ 100; 2 ≤ k ≤ 100) — the endpoint and the constraint on the jumps, respectively.

Output
For each testcase, in the first line, print a single integer n — the smallest number of moves it takes the grasshopper to reach point x.

In the second line, print n integers, each of them not divisible by k. A positive integer would mean jumping to the right, 
a negative integer would mean jumping to the left. The endpoint after the jumps should be exactly x.

Each jump distance should be from −10^9 to 10^9. 
In can be shown that, for any solution with the smallest number of jumps, there exists a solution with the same number of jumps such that each jump is from −10^9 to 10^9.

It can be shown that the answer always exists under the given constraints. If there are multiple answers, print any of them.

Input:
3
10 2
10 3
3 4

Output:
2
7 3
1
10
1
3
"""
cases = int(input())
for i in range(cases):
    x, k = map(int, input().split())
    if(x % k != 0):
        print(1)
        print(x)
    else:
        print(2)
        print(1, x - 1)
