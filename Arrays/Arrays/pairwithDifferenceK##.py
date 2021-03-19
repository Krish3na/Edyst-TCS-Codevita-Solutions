def solve(l,k):
    low=0
    high=1
    while low<high and high <=len(l)-1 and low <=len(l)-2:
        diff=abs(l[low]-l[high])
        #print(diff)
        if diff==k:
            return 1
        if diff < k:
            high +=1
        if diff > k:
            low +=1
            if low==high:
                high+=1
        
    return 0

t=int(input())
for _ in range(t):
    l=list(map(int,input().strip().split()))
    k=int(input())
    #print(k)

    l.sort()
    #print(l)
    print(solve(l,k))
