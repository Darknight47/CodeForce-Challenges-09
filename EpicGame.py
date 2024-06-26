"""

------------------- Link for the challenge: https://codeforces.com/problemset/problem/119/A -----------------------

Simon and Antisimon play a game. Initially each player receives one fixed positive integer that doesn't change throughout the game. Simon receives number a and Antisimon receives number b. 
They also have a heap of n stones. The players take turns to make a move and Simon starts. During a move a player should take from the heap the number of stones equal to 
the greatest common divisor of the fixed number he has received and the number of stones left in the heap. A player loses when he cannot take the required number of stones 
(i. e. the heap has strictly less stones left than one needs to take).

Your task is to determine by the given a, b and n who wins the game.

Input
The only string contains space-separated integers a, b and n (1 ≤ a, b, n ≤ 100) — the fixed numbers Simon and Antisimon have received correspondingly and the initial number of stones in the pile.

Output
If Simon wins, print "0" (without the quotes), otherwise print "1" (without the quotes).

Input:
3 5 9

Output:
0
"""
import math
a, b, n = map(int, input().split())
simon = True
while True:
    if(simon):
        gcd = math.gcd(a, n)
        if(gcd <= n):
            n -= gcd
        else:
            print(1)
            break
        simon = False
    else:
        gcd = math.gcd(b, n)
        if(gcd <= n):
            n -= gcd
        else:
            print(0)
            break
        simon = True
