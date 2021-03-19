nc=int(input())
ct=list(map(int,input().split()))
q,r=map(int,input().split())
ans=[]
for i in range(q):
    l=list(map(int,input().split()))
    ct[l[0]-1]=l[1]
    ct.sort()
    #print(ct)
    ans.append(ct[l[2]-1])
for i in ans:
    print(i,end=' ')


