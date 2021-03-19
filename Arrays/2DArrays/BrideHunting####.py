'''
Codevita [2018] Bride Hunting
Bride Hunting
Sam is an eligible bachelor. He decides to settle down in life and start a family. He goes bride hunting.

He wants to marry a girl who has at least one of the 8 qualities mentioned below:-

The girl should be rich
The girl should be an Engineer/Doctor
The girl should be beautiful
The girl should be of height 5.3"
The girl should be working in an MNC
The girl should be an extrovert
The girl should not have spectacles
The girl should be kind and honest
He is in search of a bride who has some or all of the 8 qualities mentioned above. On bride hunting, he may find more than one contenders to be his wife.

In that case, he wants to choose a girl whose house is closest to his house. Find a bride for Sam who has maximum qualities. If in case, there are more than one contenders who are at equal distance from Sam’'s house; then

print Polygamy not allowed

In case there is no suitable girl who fits the criteria then print No suitable girl found

Given a Matrix N*M, Sam’s house is at (1, 1). It is denoted by 1. In the same matrix, the location of a marriageable Girl is also denoted by 1. Hence 1 at location (1, 1) should not be considered as the location of a marriageable Girl’s location.
The qualities of that girl, as per Sam’'s criteria, have to be decoded from the number of non-zero neighbors (max 8-way) she has. Similar to the condition above, 1 at location (1, 1) should not be considered as the quality of a Girl. See Example section to get a better understanding.
Find Sam, a suitable Bride and print the row and column of the bride, and find out the number of qualities that the Bride possesses.
Distance is calculated in number of hops in any direction i.e. (Left, Right, Up, Down and Diagonal)
Constraints
2 <= N,M <= 10^2
Input Format
First Line contains the row (N) and column (M) of the houses.
Next N lines contain the data about girls and their qualities.

Output
It will contain the row and column of the bride, and the number of qualities that Bride possess separated by a colon (i.e. :).

Explanation
Input:

2 9
1 0 1 1 0 1 1 1 1
0 0 0 1 0 1 0 0 1
Output:

1:7:3
Explanation:

The girl and qualities are present at (1,3),(1,4),(1,6),(1,7),(1,8),(1,9),(2,4),(2,6),(2,9).
The girl present at (1,3) has 2 qualities (i.e. (1,4)and (2,4)).
The girl present at (1,4) has 2 qualities.
The Bride present at (1,6) has 2 qualities.
The Bride present at (1,7) has 3 qualities.
The Bride present at (1,8) has 3 qualities.
The Bride present at (1,9) has 2 qualities.
The Bride present at (2,4) has 2 qualities.
The Bride present at (2,6) has 2 qualities.
The Bride present at (2,9) has 2 qualities.
As we see, there are two contenders who have maximum qualities, one is at (1,7) and another at (1,8).
The girl who is closest to Sam’s house is at (1,7). Hence, she is the bride.
Hence, the output will be 1:7:3.

Input:

6 6
1 0 0 0 0 0
0 0 0 0 0 0
0 0 1 1 1 0
0 0 1 1 1 0
0 0 1 1 1 0
0 0 0 0 0 0
Output:

4:4:8
Explanation:

The bride and qualities are present at (3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)
The Bride present at (3,3) has 3 qualities (i.e. (3,4),(4,3) and (4,4)).
The Bride present at (3,4) has 5 qualities.
The Bride present at (3,5) has 3 qualities.
The Bride present at (4,3) has 5 qualities.
The Bride present at (4,4) has 8 qualities.
The Bride present at (4,5) has 5 qualities.
The Bride present at (5,3) has 3 qualities.
The Bride present at (5,4) has 5 qualities.
The Bride present at (5,5) has 3 qualities.
As we see, the girl present in (4,4) has maximum number of Qualities. Hence, she is the bride.

Hence, the output will be 4:4:8.

'''

def check(a):
    i,j = a[0],a[1]
    cnt=0

    if mat[i][j-1] == 1 :  
        cnt+=1
    if mat[i][j+1] == 1:
        cnt+=1
    if mat[i-1][j] == 1:
        cnt+=1
    if mat[i+1][j] == 1 :
        cnt+=1
    if mat[i-1][j-1] == 1 :
        cnt+=1
    if mat[i-1][j+1] == 1 :
        cnt+=1
    if mat[i+1][j-1] == 1 :
        cnt+=1
    if mat[i+1][j+1] == 1 :
        cnt+=1
    #print(cnt)
    distance = round(((i-1)**2 + (j-1)**2)**0.5)
    return cnt,distance

n,m=map(int,input().split())
mat=[[0 for j in range(m+2)] for i in range(n+2)]
for i in range(1,n+1):
    l=list(map(int,input().split()))
    for j in range(1,m+1):
        mat[i][j]=l[j-1]   
count=0
ind={}
for i in range(1,n+1):
    for j in range(1,m+1):
        if  mat[i][j]==1:
            if i==1 and j==1 :
                continue
            index=(i,j)
            count,distance=check(index)
            ind[index]=(count,distance)
#print(ind)
max_c=0
min_dis=1000000
fkey=0
final={}
for key in ind.keys():
    k,m,d=key,ind[key][0],ind[key][1]
    if m>max_c :
        fkey,max_c,min_dis=k,m,d


for key in ind.keys():
    k,m,d=key,ind[key][0],ind[key][1]
    if m==max_c and d==min_dis and k!=fkey:
        print('Polygamy not allowed')
        exit(0)

if fkey!=0:
    print(fkey[0],fkey[1],ind[fkey][0],sep=':')

else:
    print('No suitable girl found')

