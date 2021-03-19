'''
Print intersection of 2 Sorted Arrays
Intersection of 2 Sorted Arrays
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Input Format
The first line contains T, the number of test cases. Following T lines contain:
Line 1 contains N1, followed by N1 integers of the first array
Line 2 contains N2, followed by N2 integers of the second array
Output Format
The intersection of the arrays in a single line

Example
Input:
1
3 10 17 57
6 2 7 10 15 57 246

Output:

10 57

Input:
1
6 1 2 3 3 4 5 6
2 1 6

Output:
1 6
'''

def intersection(a1,a2):
    #print(a1)
    #print(a2)
    p1,p2=0,0
    while p1<len(a1) and p2<len(a2):
        if a1[p1]==a2[p2] :
            print(a1[p1],end=' ')
            p1+=1
            p2+=1
        elif a1[p1]<a2[p2]:
            p1+=1
        else :
            p2+=1
    print()

t=int(input())
for _ in range(t):
    arr1=list(map(int,input().split()))
    #arr1.sort()
    arr2=list(map(int,input().split()))
    #arr2.sort()
    
    intersection(arr1[1:],arr2[1:])
