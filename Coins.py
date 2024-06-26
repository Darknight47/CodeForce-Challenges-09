"""
In Berland, there are two types of coins, having denominations of 2
 and k
 burles.

Your task is to determine whether it is possible to represent n
 burles in coins, i. e. whether there exist non-negative integers x
 and y
 such that 2⋅x+k⋅y=n
.

Input
The first line contains a single integer t
 (1≤t≤104
) — the number of test cases.

The only line of each test case contains two integers n
 and k
 (1≤k≤n≤1018
; k≠2
).

Output
For each test case, print YES if it is possible to represent n
 burles in coins; otherwise, print NO. You may print each letter in any case (YES, yes, Yes will all be recognized as positive answer, NO, no and nO will all be recognized as negative answer).

"""
cases = int(input())
for i in range(cases):
    n, k = map(int, input().split())
    if(n % 2 == 1 and k % 2 == 0):
        print("NO")
    else:
        print("YES")