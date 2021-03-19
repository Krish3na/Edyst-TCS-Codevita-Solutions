'''
Codevita [2014] Matrix Rotations
Matrix Rotations
You are given a square matrix of dimension N. Let this matrix be called A. Your task is to rotate A in clockwise direction byS degrees, where S is angle of rotation. On the matrix, there will be 3 types of operations viz.

Rotation
Rotate the matrix A by angle S, presented as input in form of A S

Querying
Query the element at row K and column L, presented as input in form of Q K L

Updation
Update the element at row X and column Y with value Z, presented as input in form of U X Y Z

Print the output of individual operations as depicted in Output Specification

Input Format:
Input will consist of three parts, viz.

Size of the matrix (N)
The matrix itself (A = N * N)
Various operations on the matrix, one operation on each line. (Beginning either with A, Q or U)
-1 will represent end of input
Note:

Angle of rotation will always be multiples of 90 degrees only.
All Update operations happen only on the initial matrix. After update all the previous rotations have to be applied on the updated matrix
Output Format:
For each Query operation print the element present at K-L location of the matrix in its current state.

Constraints:
1<=N<=1000
1<=Aij<=1000
0<=S<=160000
1<=K, L<=N
1<=Q<=100000
Sample Input and Output
Input

2
1 2
3 4
A 90
Q 1 1
Q 1 2
A 90
Q 1 1
U 1 1 6
Q 2 2
-1
Output

3
1
4
6
Explanation:

Initial Matrix
1 2
3 4

After 90 degree rotation, the matrix will become
3 1
4 2

Now the element at A11 is 3 and A12 is 1.

Again the angle of rotation is 90 degree, now after the rotation the matrix will become
4 3
2 1
Now the element at A11 is 4.

As the next operation is Update, update initial matrix i.e.
6 2
3 4

After updating, apply all the previous rotations (i.e. 180 = two 90 degree rotations)
The matrix will now become
4 3
2 6
Now A22 is 6.

'''
def rotate( m ,angle):
    if angle>=360:
        angle=angle%360
    rotations=angle//90
    for k in range(0,rotations):
        new_mat = []
        for j in range(0, len(m[0])):
            l = []
            for i in range(len(m) - 1, -1, -1):
                l.append(m[i][j])
            new_mat.append(l)
        m=new_mat
    return m

n=int(input())
mat=[]
for i in range(0,n):
    mat.append(list(map(int,input().split())))
angle=0
l=mat
while True:
    ques=input().split()
    if ques=="-1":
        break
    if ques[0]=='A':
        l=rotate(l,int(ques[1]))
        angle=angle+int(ques[1])
    elif ques[0]=='Q':
        k = int(ques[1]) - 1
        z = int(ques[2]) - 1
        print(l[k][z])
    elif ques[0]=='U':
        k=int(ques[1])-1
        z=int(ques[2])-1
        val=int(ques[3])
        mat[k][z]=val
        l=rotate(mat,angle)
    else:
        break
