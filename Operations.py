"""

---------------- Link for the challenge: https://codeforces.com/problemset/problem/1556/A ---------------------

William has two numbers a and b initially both equal to zero. William mastered performing three different operations with them quickly. Before performing each operation some positive integer k 
is picked, which is then used to perform one of the following operations: (note, that for each operation you can choose a new positive integer k)

add number k to both a and b, or
add number k to a and subtract k from b , or add number k to b and subtract k from a.
Note that after performing operations, numbers a and b may become negative as well.

William wants to find out the minimal number of operations he would have to perform to make a qual to his favorite number c and b equal to his second favorite number d.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). Description of the test cases follows.

The only line of each test case contains two integers c and d (0 ≤ c, d ≤ 10^9), which are William's favorite numbers and which he wants a and b to be transformed into.

Output
For each test case output a single number, which is the minimal number of operations which William would have to perform to make a 
equal to c and b equal to d, or −1 if it is impossible to achieve this using the described operations.

Input:
6
1 2
3 5
5 3
6 6
8 0
0 0

Output:
-1
2
2
1
2
0
"""
cases = int(input())
for i in range(cases):
    c, d = map(int, input().split())
    if(c == 0 and d == 0):
        print(0)
    elif(c == d):
        print(1)
    elif(abs(c - d) % 2 == 0):
        print(2)
    else:
        print(-1)