"""

-------------- Link for the challenge: https://codeforces.com/problemset/problem/1669/C ---------------------- 

Given an array a=[a1,a2,…,an] of n positive integers, you can do operations of two types on it:

Add 1 to every element with an odd index. In other words change the array as follows: a1:=a1+1,a3:=a3+1,a5:=a5+1,.
Add 1 to every element with an even index. In other words change the array as follows: a2:=a2+1,a4:=a4+1,a6:=a6+1,….
Determine if after any number of operations it is possible to make the final array contain only even numbers or only odd numbers. 
In other words, determine if you can make all elements of the array have the same parity after any number of operations.

Note that you can do operations of both types any number of times (even none). Operations of different types can be performed a different number of times.

Input
The first line contains an integer t (1 ≤ t ≤ 100) — the number of test cases.

The first line of each test case contains an integer n (2 ≤ n ≤ 50) — the length of the array.

The second line of each test case contains n
integers a1,a2,…,an (1 ≤ a(i) ≤ 10^3) — the elements of the array.

Note that after the performed operations the elements in the array can become greater than 10^3.

Output
Output t lines, each of which contains the answer to the corresponding test case. As an answer, output "YES" if after any number of operations 
it is possible to make the final array contain only even numbers or only odd numbers, and "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).

Input:
4
3
1 2 1
4
2 2 2 3
4
2 2 2 2
5
1000 1 1000 1 1000

Output:
YES
NO
YES
YES
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    a = list(map(int, input().split()))

    even1 = even2 = odd1 = odd2 = 0
    for i in range(n):
        if i % 2 == 0:
            if a[i] % 2 == 1:
                odd1 = 1
            else:
                even1 = 1
        else:
            if a[i] % 2 == 1:
                odd2 = 1
            else:
                even2 = 1

    if even1 and odd1:
        print("NO")
    elif even2 and odd2:
        print("NO")
    else:
        print("YES")
