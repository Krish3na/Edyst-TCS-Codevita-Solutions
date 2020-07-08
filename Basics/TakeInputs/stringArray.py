'''
Input String Array
Input String Array
Write a program that takes as input String arrays and prints the String arrays

Input Format
The first line contains N, the number of test cases.

The N lines after that contain the test cases
Each test case starts with k, the number of elements in the array
This is followed by k elements of the array
Output Format
Print each array in a single line

Sample Input / Output
Input
3
1 hello
5 hello welcome to the codevita
8 there is nothing better than coding agreed ?

Output
hello
hello welcome to the codevita
there is nothing better than coding agreed ?
'''

N=int(input())
for i in range(N):
    x=list(map(str,input().split()))
    for i in range(1,len(x)):
        print(x[i],end=" ")
    print()    
        
