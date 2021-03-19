'''

def solve(s):
    dic={}
    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1

    max_char=max(dic,key=lambda x:dic[x])
    max_count=dic[max_char]
    return(max_char*max_count)

n=int(input())
for i in range(n):
    s=input()
    print(solve(s))

def solve(l,x):
    l.sort()
    for i in l:
        if i>0:
            ind=l.index(i)
            break
            
    newl=l[ind:]
    nl=l[:ind]

    tot=0

    if x==0:
        for i in newl:
            tot+=i
        return tot
    if x>0:
        for i in newl:
            tot+=i*x
        for i in nl:
            tot+=i
        return tot
    if x<0:
        for i in newl:
            tot+=i
        for i in nl:
            tot+=i*x
        return tot

import math
def sumofDivisors(n): 
  
    m = dict() 
    for j in range(2, math.ceil(math.sqrt(n))): 
  
        count = 0
        while (n % j == 0): 
            n //= j 
            count += 1
  
        if (count): 
            m[j] = count 
 
    if (n != 1): 
        m[n] = 1
  
    ans = 1
    for it in m: 
        pw = 1
        summ = 0
  
        for i in range(m[it] + 1, 0, -1): 
            summ += (i * pw) 
            pw *= it 
      
        ans *= summ 
  
    return (ans) 
t=int(input())
for i in range(t):
    n=int(input())
    for j in range(n):
        a=int(input())
        tot=0
        for i in range(1,a+1):
            if a%i==0:
                tot+=i
        lis.append(tot)
        print(tot,end=' ')
'''
a=int(input())
lis=[]

for j in range(1,a+1):
    tot=0
    for i in range(1,j+1):
        if j%i==0:
            tot+=i
    lis.append(tot)
print(lis)
    
'''

def solve(l,x):
    l.sort()
    for i in l:
        if i>0:
            ind=l.index(i)
            break
            
    newl=l[ind:]
    nl=l[:ind]

    tot=0

    if x==0:
        for i in newl:
            tot+=i
        return tot
    if x>0:
        for i in newl:
            tot+=i*x
        for i in nl:
            tot+=i
        return tot
    if x<0:
        for i in newl:
            tot+=i
        for i in nl:
            tot+=i*x
        return tot


t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    print(solve(l,x))
'''
