"""

------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1842/A -----------------------

Tsondu and Tenzing are playing a card game. Tsondu has n monsters with ability values a1,a2,…,an while Tenzing has m monsters with ability values b1,b2,…,bm.

Tsondu and Tenzing take turns making moves, with Tsondu going first. In each move, the current player chooses two monsters: one on their side and one on the other side. 
Then, these monsters will fight each other. Suppose the ability values for the chosen monsters are x and y respectively, 
then the ability values of the monsters will become x−y and y−x respectively. If the ability value of any monster is smaller than or equal to 0, the monster dies.

The game ends when at least one player has no monsters left alive. The winner is the player with at least one monster left alive. If both players have no monsters left alive, the game ends in a draw.

Find the result of the game when both players play optimally.

Input
Each test contains multiple test cases. The first line of input contains a single integer t (1 ≤ t ≤ 2⋅10^3) — the number of test cases. The description of test cases follows.

The first line of each test case contains two integers n and m (1 ≤ n , m ≤ 50) — the number of monsters Tsondu and Tenzing have respectively.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9) — the ability values of Tsondu's monsters.

The third line of each test case contains m integers b1,b2,…,bm (1 ≤ b(i) ≤ 10^9) — the ability values of Tenzing's monsters.

Output
For each test case, output "Tsondu" if Tsondu wins, "Tenzing" if Tenzing wins, and "Draw" if the game ends in a draw. (Output without quotes.)

Note that the output is case-sensitive. For example, if the answer is "Tsondu", the outputs "tsondu", "TSONDU", and "tSonDu" will all be recognized as incorrect outputs.

Input:
6
1 3
9
1 2 3
2 3
1 2
1 1 1
3 2
1 2 3
1 1
3 3
1 1 1
2 2 2
10 10
1 2 3 3 2 2 1 1 2 2
3 3 3 3 2 1 1 1 1 1
10 10
1 2 3 4 5 6 7 8 9 10
6 7 8 9 10 11 1 1 1 1

Output:
Tsondu
Draw
Tsondu
Tenzing
Draw
Draw
"""
cases = int(input())
for i in range(cases):
    n, m = map(int, input().split())
    tsondos = list(map(int, input().split()))
    tenzings = list(map(int, input().split()))
    tsondoSum = sum(tsondos)
    tenzingSum = sum(tenzings)
    diff = tsondoSum - tenzingSum
    if(diff == 0):
        print("Draw")
    elif(diff < 0):
        print("Tenzing")
    else:
        print("Tsondu")