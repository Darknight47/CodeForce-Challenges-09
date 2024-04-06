"""

---------------- Link for the challenge: https://codeforces.com/problemset/problem/1886/A ----------------

Monocarp has an integer n.

He wants to represent his number as a sum of three distinct positive integers x, y, and z. 
Additionally, Monocarp wants none of the numbers x , y, and z to be divisible by 3.

Your task is to help Monocarp to find any valid triplet of distinct positive integers x, y, and z, or report that such a triplet does not exist.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of testcases.

The only line of each testcase contains a single integer n (1 ≤ n ≤ 10^9).

Output
For each testcase, if there is no valid triplet x, y, and z, print NO on the first line.

Otherwise, print YES on the first line. On the second line, print any valid triplet of distinct positive integers x, y, and z such that x+y+z=n, and none of the printed numbers are divisible by 3. 
If there are multiple valid triplets, you can print any of them.

Input:
4
10
4
15
9

Output:
YES
4 5 1
NO
YES
2 8 5
NO
"""

cases = int(input())
for i in range(cases):
    temp = int(input())
    first = 1
    second = 2
    third = -1
    while True:
        tt = abs(temp - (first + second))
        if(tt % 3 == 0):
            while True:
                second += 1
                if(second % 3 != 0):
                    break
        else:
            third = tt
            break
    tempSet = set()
    tempSet.add(first)
    tempSet.add(second)
    tempSet.add(third)
    if(len(tempSet) == 3 and ((first + second + third) == temp)):
        print("YES")
        print(first, second, third)
    else:
        print("NO")