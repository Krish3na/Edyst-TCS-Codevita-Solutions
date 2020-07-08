'''
Lazy Student
There is a test of Algorithms. Teacher provides a question bank consisting of N questions and guarantees all the questions in the test will be from this question bank. Due to lack of time and his laziness, Codu could only practice M questions. There are T questions in a question paper selected randomly. Passing criteria is solving at least 1 of the T problems. Codu can't solve the question he didn't practice. What is the probability that Codu will pass the test?

Constraints
0 < K <= 10000
0 < N, T <= 1000
0 <= M <= 1000
M,T <= N
Input Format
First line contains single integer K denoting the number of test cases.
First line of each test case contains 3 integers separated by space denoting N, T, and M.
Output
For each test case, print a single integer.
If probability is p/q where p & q are co-prime, print  (p*mulInv(q)) modulo 1000000007, where mulInv(x) is multiplicative inverse of x under modulo 1000000007.
Example Input 1
1
4 2 1
Output
500000004
Explanation
The probability is 1/2. So output is 500000004
'''


import math

k=int(input())
max_n=1000
prime=(10**9)+7

def mult(a,b,prime):
    ans = (a%prime * b%prime)%prime
    return ans

def exp(p,q,prime):
    if q==1:
        return p%prime
    if q==0:
        return 1
    temp=exp(p,q//2,prime)
    ans=mult(temp,temp,prime)
    if q%2==0:
        return ans
    else:
        return mult(ans,p,prime)

#pascal
pascal=[[0 for i in range(max_n+1)] for j in range(max_n+1)]
pascal[0][0]=1
for i in range(1,len(pascal)):
    pascal[i][0]=1
    for j in range(1,i+1):
        pascal[i][j]=(pascal[i-1][j-1] + pascal[i-1][j])%prime
        
for case in range(k):
    n, t, m= list(map(int,input().split()))
    if n-m<t:
        print(1)
        continue
    if m==0:
        print(0)
        continue
    denominator=pascal[n][t]
    numerator=pascal[n-m][t]
        
    p=denominator-numerator
    q=denominator
    
    #reducing them
    common=math.gcd(p,q)
    p= p//common
    q= q//common
       
    q_inv = pow(q,prime-2,prime)
    ans=mult(p,q_inv,prime)
        
    print(ans)
