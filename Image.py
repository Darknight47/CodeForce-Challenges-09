"""
------------------ Link for the challenge: https://codeforces.com/problemset/problem/1721/A -----------------------

You have an image file of size 2×2, consisting of 4 pixels. Each pixel can have one of 26 different colors, denoted by lowercase Latin letters.

You want to recolor some of the pixels of the image so that all 4 pixels have the same color. 
In one move, you can choose no more than two pixels of the same color and paint them into some other color 
(if you choose two pixels, both should be painted into the same color).

What is the minimum number of moves you have to make in order to fulfill your goal?

Input
The first line contains one integer t (1 ≤ t ≤ 1000) — the number of test cases.

Each test case consists of two lines. Each of these lines contains two lowercase letters of Latin alphabet without any separators, denoting a row of pixels in the image.

Output
For each test case, print one integer — the minimum number of moves you have to make so that all 4 pixels of the image have the same color.

Input:
5
rb
br
cc
wb
aa
aa
ab
cd
yy
xx

Output:
1
2
0
3
1
"""
cases = int(input())
for i in range(cases):
    s1 = input()
    s2 = input()
    tempSet = set(s1 + s2)
    if(len(tempSet) == 1):
        ans = 0
    elif(len(tempSet) == 2):
        ans = 1
    elif(len(tempSet) == 3):
        ans = 2
    else:
        ans = 3
    print(ans)