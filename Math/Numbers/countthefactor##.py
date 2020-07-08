'''
CodeVita 2014, Count the factor
Count the Factor
The factorial of a non-negative integer N, denoted by N!, is the product of all positive integers less than and equal to N.
Factorial of any number can be represented in simplest form of its prime factors.
e.g. 4!=4*3*2*1= 2^3 * 3^1 (where ^ means exponent)

Factorials can also be specified by the number of times each prime factors occurs in it, thus 24 could be specified as (3 1) meaning 3 twos, 1 three.

Write a program that will take an integer as input and give output as the following.

Input Format
Input will be a positive integer N where N>1.
Line 1: N,where N is any integer.

Output Format
Output will show a series consists of the number of times each prime factor appears after the factorization of N! separated by spaces.

For Valid Input, print

L, where L is the series consists of the number of times each prime factor appears after the factorization of N! separated by spaces.

For Invalid Input,print

Invalid Input

Sample Test Cases
Input
6

Output
4 2 1

Input
a

Output
Invalid Input

Input
-5

Output
Invalid Input
'''

from collections import Counter
l=[]
def primeFactors(n):
    while n % 2 == 0:
        l.append(2)
        n = n // 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            l.append(i)
            n = n // i
    if n > 2:
        l.append(n)
        
n=input()
if(not n.isdigit() or int(n)<=0):
    print("Invalid Input")
else:
    for i in range(2,int(n)+1):
        primeFactors(i) 
   
    d=dict(Counter(l))
    for k,v in d.items():
        print(v,end=' ')
    print()
