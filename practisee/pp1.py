t=int(input())
for i in range(t):
    a,k,h=map(int,input().split())
    cal=list(input())
    tot=0
    for j in cal:
        if j=='P':
            a=a*k
            #tot+=a
        if j=='E':
            tot+=a
            print(tot)

    print(tot)
    
