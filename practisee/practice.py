'''
a=str(input())
b=str(input())
c=str(input())
p=min(a[0],b[0],c[0])
q=min(a[1],b[1],c[1])
r=min(a[2],b[2],c[2])
s=min(a[3],b[3],c[3])

print(int(p+q+r+s))

#####a###################################
st=[]
ust=[]
flag=0
l=list(map(str,input().split()))
for i in l:
    b=set(i)
    t=len(i)%len(b)
    if t==0:
        st.append(int(i))        
    else:
        ust.append(int(i))
print(st,ust)



print(max(st)-min(ust))
    
'''

t=int(input())
for i in range(t):
    n=int(input())
    for k in range(1,n+1):
        for j in range(1,k+1):
            print(j,end=' ')
        print()



