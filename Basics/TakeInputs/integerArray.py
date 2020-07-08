'''
Input Integer Array
Input Integer Array
Write a program that takes as input integer arrays and prints the integer arrays

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
1 27
5 19 2893 3497 9 876
8 19 2893 890 3497 -293 9 876 -98
Output

27
19 2893 3497 9 876
19 2893 890 3497 -293 9 876 -98
'''

N=int(input())
for i in range(N):
    x=list(map(int,input().split()))
    for i in range(1,len(x)):
        print(x[i],end=" ")
    print()
    
