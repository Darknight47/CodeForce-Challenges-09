"""

------------------ Link for the challenge: https://codeforces.com/contest/1234/problem/B1 ----------------------

The only difference between easy and hard versions are constraints on n and k.

You are messaging in one of the popular social networks via your smartphone. Your smartphone can show at most k
most recent conversations with your friends. Initially, the screen is empty (i.e. the number of displayed conversations equals 0).

Each conversation is between you and some of your friends. There is at most one conversation with any of your friends. So each conversation is uniquely defined by your friend.

You (suddenly!) have the ability to see the future. You know that during the day you will receive n
messages, the i-th message will be received from the friend with ID idi (1 ≤ idi ≤ 10^9).

If you receive a message from idi in the conversation which is currently displayed on the smartphone then nothing happens: 
the conversations of the screen do not change and do not change their order, you read the message and continue waiting for new messages.

Otherwise (i.e. if there is no conversation with idi on the screen):

Firstly, if the number of conversations displayed on the screen is k , the last conversation (which has the position k) is removed from the screen.
Now the number of conversations on the screen is guaranteed to be less than k and the conversation with the friend idi is not displayed on the screen.
The conversation with the friend idi appears on the first (the topmost) position on the screen and all the other displayed conversations are shifted one position down.
Your task is to find the list of conversations (in the order they are displayed on the screen) after processing all n messages.

Input
The first line of the input contains two integers n and k (1 ≤ n, k ≤ 200) — the number of messages and the number of conversations your smartphone can show.

The second line of the input contains n integers id1,id2,…,idn (1 ≤ idi ≤ 10^9), where idi is the ID of the friend which sends you the i-th message.

Output
In the first line of the output print one integer m (1 ≤ m ≤ min(n,k)) — the number of conversations shown after receiving all n messages.

In the second line print m integers ids1,ids2,…,idsm , where idsi should be equal to the ID of the friend corresponding to the conversation displayed on the position i after receiving all n messages.

Input:
7 2
1 2 3 2 1 3 2

Output:
2
2 1 
"""

import queue
messages, conversations = map(int, input().split())
lstIDs = list(map(int, input().split()))
q = queue.Queue()
tempLst = []
for i in range(messages):
    tempID = lstIDs[i]
    if(tempID not in tempLst):
        if(q.qsize() == conversations):
            q.get()
        q.put(tempID)
    tempLst = list(q.queue)
print(len(tempLst))
for indx in reversed(tempLst):
    print(indx, end=" ")
print("")