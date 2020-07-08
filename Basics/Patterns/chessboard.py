'''
Print Simple Chessboard
Simple Chessboard
Write a program that prints a simple chessboard.

Input format:
The first line contains the number of inputs T.
The lines after that contain a different values for size of the chessboard
Output format:
Print a chessboard of dimensions size * size. Print a Print W for white spaces and B for black spaces.

Input:
2
3
5

Output:
WBW
BWB
WBW
WBWBW
BWBWB
WBWBW
BWBWB
WBWBW
'''
n=int(input())
for i in range(n):
    x=int(input())
    for j in range(1,x+1):
        for k in range(1,x+1):
            if (j+k)%2!=0:
                print("B",end="")
            else:
                print("W",end="")
        print()

'''
Print Our Own Chessboard
Our Own Chessboard
Let’s print a chessboard!

Write a program that takes input:

The first line contains T, the number of test cases
Each test case contains an integer N and also the starting character of the chessboard
Output Format
Print the chessboard as per the given examples

Sample Input / Output
Input:
2
2 W
3 B

Output:
WB
BW
BWB
WBW
BWB
'''
t=int(input())
for i in range(t):
    x=list(map(str,input().split()))
    if x[1]=='W':
        for i in range(1,int(x[0])+1):
            for j in range(1,int(x[0])+1):
                if (i+j)%2!=0:
                    print("B",end="")
                else:
                    print("W",end="")
            print()
    else:
        if x[1]=='B':
            for i in range(1,int(x[0])+1):
                for j in range(1,int(x[0])+1):
                    if (i+j)%2!=0:
                        print("W",end="")
                    else:
                        print("B",end="")
                print()
