'''
Input Integers
Input Integer
Write a program that takes as input integers and prints the integers.

Input Format
The first line contains N, the number of test cases.

The line after that contains N space separated integers in 1 line

Output Format
Print each integer in a single line

Sample Input / Output
Input
5
7 89 101 30 42

Output
7
89
101
30
42
'''

N=int(input())
x=list(map(int,input().split()))
for i in range(N):
    print(x[i])

