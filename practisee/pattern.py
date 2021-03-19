
'''

t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l=[0]+l+[0]
    gifts=[0]*(n+1)
    ngifts=0
    maxrank=0
    for i in range(1,n+1):
        if l[i]>l[i-1]:
            ngifts+=1
            gifts[i-1]+=ngifts
            #maxrank=l[i]
        else:
            if ngifts!=1:
                ngifts-=1
            gifts[i-1]+=ngifts
    
    print(sum(gifts))

    


n,k=map(int,input().split())
l=list(map(int,input().split()))
count=0
for i in range(n):
    ran_l=l[i]-k
    ran_u=l[i]+k
    state=0
    for x in range(n):
        if not (i==x):
            if ran_l <= l[x] <= ran_u:
                state=1
    count += 1 if state ==1 else 0
print(count)



for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    ltor=[1]*n
    rtol=[1]*n
    sum=0
    for i in range(1,n):
        if(li[i]>li[i-1]):
            ltor[i]=ltor[i-1]+1

    for i in range(n-2,-1,-1):
        if(li[i]>li[i-1]):
            rtol[i]=rtol[i-1]+1
    for i in range(n):
        sum+=max(ltor[i],rtol[i])
         
    print(sum)

'''

def count(elemlst) :
    cont=0
    for i in range(n):
        a=elemlst[i]
        id1=i
        id2=i
        if i==0:
            while elemlst[id2+1]==a:
                id2+=1
            if elemlst[id2+1]<=a+z and elemlst[id2+1]>=a-z:
                cont+=1
        elif i<n-1:
            while elemlst[id2+1]==a:
                 id2+=1
            while elemlst[id1-1]==a:
                 id1-=1
            if (elemlst[id1-1]<=a+z and elemlst[id1-1]>=a-z) or (elemlst[id2+1]<=a+z and elemlst[id2+1]>=a-z):
                 cont+=1
        else:
            while elemlst[id1-1]==a:
                id1-=1
            if elemlst[id1-1]<=a+z and elemlst[id1-1]>=a-z:
                cont+=1
    return cont
n,z=map(int,input().split())
elemlst=list(map(int,input().split()))
elemlst.sort()
print(count(elemlst))
