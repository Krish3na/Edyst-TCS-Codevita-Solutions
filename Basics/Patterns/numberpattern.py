'''
Print Number Pattern
Number Pattern
Write a program that reads an input n from stdin. n tells us the number of rows to be printed. Print the pattern as per the given examples.

Input format: The first line contains the number of inputs T. The lines after that contain a different values for n

Output format: Print the pattern as per the example

Example Input:
2
3
5
Output:
1
1 2
1 2 3
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


'''
t=int(input())
for i in range(t):
    x=int(input())
    for i in range(1,x+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
    


