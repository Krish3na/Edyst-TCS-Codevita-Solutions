'''

Castle Arbitrage
You are building a house of cards. No, a castle of cards!

You have cards of 3 sizes l, m and n. To build a house of height exactly H, you can as many of these cards as you want.

Find the number of ways you can reach to a height exactly H, given you have unlimited cards of l, m and n sizes

Constraints
l,m,n <= H <= 106
l, m, n are distinct
Input format
The first line contains H, the desired height
The next line contains 3 space-separated integers l, m and n respectively
Output
Print the number of ways it's possible to reach a height H. The output may be very large, so print your answer mod 109+7
If no combination is possible, print 0
Example Input
10
2 4 8
Output
10
Explanation
We can use the following sets of cards to reach 10:

{2,2,2,2,2}
{2,2,2,4}
{2,2,4,2}
{2,4,2,2}
{4,2,2,2}
{4,4,2}
{4,2,4}
{2,4,4}
{2,8}
{8,2}

'''

a=int(input())
b=10**9+7
lst=list(map(int,input().split()))
lst.sort()
l=lst[0]
m=lst[1]
n=lst[2]
ways=[0]*(a+1)
ways[l]=1
ways[m]=1
ways[n]=1
for i in range(l,len(ways)):
    if(i>=l):
        ways[i]=(ways[i]+ways[i-l])%b
    if(i>=m):
        ways[i]=(ways[i]+ways[i-m])%b
    if(i>=n):
        ways[i]=(ways[i]+ways[i-n])%b
print(ways[a])
