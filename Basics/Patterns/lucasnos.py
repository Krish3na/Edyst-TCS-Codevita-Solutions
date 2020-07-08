'''
Print Lucas Numbers
In Lucas series, the next number is the sum of previous two numbers. The series starts with 2 and 1, and then the next numbers are a sum of the previous 2 numbers.

For example 2, 1, 3, 4, 7, 11, 18, 29, etc.

Here the first 2 numbers are 2 and 1

The next numbers are:

3 (= 1 + 2)
4 (= 3 + 1)
7 (= 4 + 3)
11 (= 7 + 4)
And so on…

Write a program the first n numbers of the Lucas series.

Hint: You already know the first 2 values. How can you calculate the remaining?

Input Format
The first line contains T the number of test cases.

The following T lines contain n, the input for the Fibonacci Series.

Output Format
Print the values on a single line, separated by a space character. At the end of the line, print a new line.

Sample Input / Output
Input
5
3
4
8
9
7

Output
2 1 3
2 1 3 4
2 1 3 4 7 11 18 29
2 1 3 4 7 11 18 29 47
2 1 3 4 7 11 18
'''

t=int(input())
for i in range(t):
    a=2
    b=1
    x=int(input())
    for i in range(x):
        c=a+b
        print(a,end=" ")
        a=b
        b=c
    print()
