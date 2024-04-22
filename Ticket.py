"""

-------------------- Link for the challenge: https://codeforces.com/problemset/problem/1941/A ------------------------

Rudolf is going to visit Bernard, and he decided to take the metro to get to him. The ticket can be purchased at a machine that accepts exactly two coins, the sum of which does not exceed k.

Rudolf has two pockets with coins. In the left pocket, there are n coins with denominations b1,b2,…,bn. In the right pocket, there are m coins with denominations c1,c2,…,cm. 
He wants to choose exactly one coin from the left pocket and exactly one coin from the right pocket (two coins in total).

Help Rudolf determine how many ways there are to select indices f and s such that bf+cs≤k.

Input
The first line contains an integer t (1 ≤ t ≤ 100) — the number of test cases. Then follows the description of each test case.

The first line of each test case contains three natural numbers n, m, and k (1 ≤ n , m ≤ 100 , 1 ≤ k ≤ 2000) — 
the number of coins in the left and right pockets, and the maximum sum of two coins for the ticket payment at the counter, respectively.

The second line of each test case contains n integers b(i) (1 ≤ b(i) ≤ 1000) — the denominations of coins in the left pocket.

The third line of each test case contains m integers c(i) (1 ≤ c(i) ≤ 1000) — the denominations of coins in the right pocket.

Output
For each testcase, output a single integer — the number of ways Rudolf can select two coins, taking one from each pocket, so that the sum of the coins does not exceed k.

Input:
4
4 4 8
1 5 10 14
2 1 8 1
2 3 4
4 8
1 2 3
4 2 7
1 1 1 1
2 7
3 4 2000
1 1 1
1 1 1 1

Output:
6
0
4
12
"""

cases = int(input())
for i in range(cases):
    n, m, k = map(int, input().split())
    arr1 = sorted(list(map(int, input().split())))
    arr2 = sorted(list(map(int, input().split())))
    ans = 0
    for tempNum in arr1:
        if(tempNum >= k):
            break
        for tempNum2 in arr2:
            if(tempNum2 >= k):
                break
            diff = tempNum + tempNum2
            if(diff <= k):
                ans += 1
            else:
                break
    print(ans)