'''

Uncertain Steps
Codu is trying to go down stairs from his building to ground floor.

He can go 3 ways:

Walk 1 step at a time.
Extend his legs and go 2 steps at a time.
Jump down 3 steps at a time.
Given n steps, calculate the number of possible ways to reach the ground floor, provided he can jump 3 steps at most once during this process.

That is, he can jump down 3 steps only once, but at any time, if he wishes, while walking down the stairs.

Constraints
1 <= N <= 1000000.
Input Format
Single Integer denoting the number of Steps, N
Output
Number of ways to reach ground floor.
As the number can be huge, give output modulo 1000000007.
Example Input 1
4
Output
7
Explanation
1, 1, 1, 1
1, 2, 1
1, 1, 2
1, 3
2, 1, 1
2, 2
3, 1
Number of ways = 7.

'''

def fibo(n):
    if n<=2:
        return fiboarr[n]
    for i in range(3,n+1):
        fiboarr.append((fiboarr[-1]+fiboarr[-2])%1000000007)
    return fiboarr[-1]
fiboarr=[1,1,2]
n=int(input())
insteps_2=(fibo(n))
#print(insteps_2)
onestep_3=0
for i in range(3,n+1):
    temp=n-i
    #print(temp)
    tempres=(fiboarr[n-(temp+3)]*fiboarr[temp])%1000000007
    #print(tempres)
    onestep_3+=tempres
print((insteps_2+onestep_3)%1000000007)
