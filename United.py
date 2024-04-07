"""
---------------- Link for the challenge: https://codeforces.com/problemset/problem/1859/A --------------------------

Given an array a of length n, containing integers. And there are two initially empty arrays b and c. 
You need to add each element of array a to exactly one of the arrays bor c, in order to satisfy the following conditions:

Both arrays b and c are non-empty. More formally, let lb be the length of array b, and lc be the length of array c. Then lb,lc≥1.
For any two indices i and j (1 ≤ i ≤ lb, 1 ≤ j ≤ lc), c(j) is not a divisor of b(i).
Output the arrays b and c that can be obtained, or output −1 if they do not exist.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 500) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (2 ≤ n ≤ 100) — the length of array a.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9) — the elements of array a.

Output
For each test case, output a single integer −1 if a solution does not exist.

Otherwise, in the first line, output two integers lb and lc — the lengths of arrays b and c respectively.

In the second line, output lb integers b1,b2,…,blb— the elements of array b.

In the third line, output lc integers c1,c2,…,clc — the elements of array c.

If there are multiple solutions, output any of them. You can output the elements of the arrays in any order.

Input:
5
3
2 2 2
5
1 2 3 4 5
3
1 3 5
7
1 7 7 2 9 1 4
5
4 8 12 12 4

Output:
-1
3 2
1 3 5 
2 4 
1 2
1 
3 5 
2 5
1 1 
2 4 7 7 9 
3 2
4 8 4 
12 12 
"""

cases = int(input())
for i in range(cases):
    sze = int(input())
    arr = sorted(list(map(int, input().split())))
    tempSet = set(arr)
    if(len(tempSet) == 1):
        print(-1)
    elif(len(tempSet) == sze):
        print(1, sze - 1)
        print(arr[0])
        for w in range(1, sze):
            print(arr[w], end = " ")
        print("")
    else:
        b = []
        cindx = -1
        for j in range(sze):
            if(len(b) == 0):
                b.append(arr[j])
            elif((len(b) >= 1) and b.count(arr[j]) > 0):
                b.append(arr[j])
            else:
                cindx = j
                break
        print(len(b), (sze - len(b)))
        print(*b)
        for z in range(cindx, sze):
            print(arr[z], end=" ")
        print("")