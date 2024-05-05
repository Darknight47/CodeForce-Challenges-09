"""

----------------- Link for the challenge: https://codeforces.com/problemset/problem/1758/A -------------------------------------

A palindrome is a string that reads the same backward as forward. For example, the strings z, aaa, ab, and abccba are palindromes, but codeforces and ab are not.

The double of a string s is obtained by writing each character twice. For example, the double of seeing is sseeeeiinng.

Given a string s, rearrange its double to form a palindrome. Output the rearranged string. It can be proven that such a rearrangement always exists.

Input
The first line of input contains t (1 ≤ t ≤ 1000) — the number of test cases.

The only line of each test case contains a single string s (1 ≤ |s| ≤ 100) consisting only of lowercase English letters.

Note that the sum of |s| over all test cases is not bounded.

Output
For each test case, output a palindromic string of length 2⋅|s| that is a rearrangement of the double of s.

Input:
4
a
sururu
errorgorn
anutforajaroftuna

Output:
aa
suurruurruus
rgnororerrerorongr
aannuuttffoorraajjaarrooffttuunnaa
"""
cases = int(input())
for i in range(cases):
    s = input()
    revS = s[::-1]
    print(s + revS)