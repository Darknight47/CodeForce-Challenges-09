"""

--------------- Link for the challenge: https://codeforces.com/problemset/problem/1925/A --------------------------

You are given two positive integers n and k.

Your task is to find a string s such that all possible strings of length n that can be formed using the first k lowercase English alphabets occur as a subsequence of s.

If there are multiple answers, print the one with the smallest length. If there are still multiple answers, you may print any of them.

Note: A string a is called a subsequence of another string b if a can be obtained by deleting some (possibly zero) characters from b without changing the order of the remaining characters.

Input
The first line of input contains a single integer t (1 ≤ t ≤ 676) denoting the number of test cases.

Each test case consists of a single line of input containing two integers n (1 ≤ n ≤ 26) and k (1 ≤ k ≤ 26).

Output
For each test case, print a single line containing a single string s which satisfies the above property. 
If there are multiple answers, print the one with the smallest length. If there are still multiple answers, you may print any of them.

Input:
4
1 2
2 1
2 2
2 3

Output:
ab
aa
baab
abcbac
"""
cases = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(cases):
    n, k = map(int, input().split())
    subStr = alphabet[:k]
    subStr = subStr * n
    print(subStr)