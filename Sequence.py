"""

---------------------- Link for the challenge: https://codeforces.com/problemset/problem/1810/A -------------------------------

A sequence of m integers a1,a2,…,am is good, if and only if there exists at least one i (1 ≤ i ≤ m) such that a(i)=i. 
For example, [3,2,3] is a good sequence, since a2=2, a3=3, while [3,1,1] is not a good sequence, since there is no i such that a(i)=i.

A sequence a is beautiful, if and only if there exists at least one subsequence of a satisfying that this subsequence is good. 
For example, [4,3,2] is a beautiful sequence, since its subsequence [4,2] is good, while [5,3,4] is not a beautiful sequence.

A sequence b is a subsequence of a sequence a if b can be obtained from a by the deletion of several (possibly, zero or all) elements.

Now you are given a sequence, check whether it is beautiful or not.

Input
Each test contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 500) — the number of test cases. Their description follows.

The first line of each test case contains an integer n (1 ≤ n ≤ 100) — the length of the given sequence.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9), representing the sequence.

Output
For each test case, output "YES" or "NO"(without quotes) in one line, representing whether the given sequence is beautiful.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.


Input:
7
3
3 2 1
4
2 4 3 5
5
2 3 5 5 6
2
3 1
5
2 4 5 2 3
4
5 6 7 8
6
6 5 4 3 2 1

Output:
YES
YES
NO
YES
YES
NO
YES
"""

cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = list(map(int, input().split()))
    haveSeenCounter = 0
    ok = False
    for j in range(sze):
        temp = lst[j]
        haveSeenCounter += 1
        if(haveSeenCounter >= temp):
            ok = True
            break
    print("YES" if ok else "NO")