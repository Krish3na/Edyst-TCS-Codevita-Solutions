'''
Input Decimals
Input decimals
Write a program that takes as input decimals and prints the decimals.

Input Format
The first line contains N, the number of test cases.

The N lines after that contain the decimals that you need to print.

Output Format
Print each decimal in a single line

Sample Input / Output
Input
3
2.5
3.99
145.678

Output
2.5
3.99
145.678

'''
N=int(input())
for i in range(N):
    x=list(map(float,input().split()))
    for j in range(len(x)):
        print(x[j])
