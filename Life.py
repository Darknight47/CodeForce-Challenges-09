"""

--------- Link for the challenge: https://codeforces.com/problemset/problem/822/A -----------------

Holidays have finished. Thanks to the help of the hacker Leha, Noora managed to enter the university of her dreams which is located in a town Pavlopolis. 
It's well known that universities provide students with dormitory for the period of university studies. Consequently Noora had to leave Vičkopolis and move to Pavlopolis. 
Thus Leha was left completely alone in a quiet town Vičkopolis. He almost even fell into a depression from boredom!

Leha came up with a task for himself to relax a little. He chooses two integers A and B and then calculates the greatest common divisor of integers "A factorial" and "B factorial". 
Formally the hacker wants to find out GCD(A!, B!). It's well known that the factorial of an integer x is a product of all positive integers less than or equal to x. 
Thus x! = 1·2·3·...·(x - 1)·x. For example 4! = 1·2·3·4 = 24. Recall that GCD(x, y) is the largest positive integer q that divides (without a remainder) both x and y.

Leha has learned how to solve this task very effective. You are able to cope with it not worse, aren't you?

Input
The first and single line contains two integers A and B (1 ≤ A, B ≤ 10^9, min(A, B) ≤ 12).

Output
Print a single integer denoting the greatest common divisor of integers A! and B!.

Input:
4 3
Output:
6
"""
import math
a, b = map(int, input().split())
if(a < b):
    print(math.factorial(a))
else:
    print(math.factorial(b))