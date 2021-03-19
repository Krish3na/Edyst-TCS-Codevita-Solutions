'''

World War E
In a crossover fantasy universe, Houin Kyoma is up in a battle against a powerful monster Nomu that can kill him in a single blow. However being a brilliant scientist Kyoma found a way to pause time for exactly M seconds. Each second, Kyoma attacks Nomu with certain power, which will reduce his health points by that exact power. Initially Nomu has H Health Points. Nomu dies when his Health Points reach 0. Normally Kyoma performs Normal Attack with power A. Besides from Kyoma’s brilliance, luck plays a major role in events of this universe. Kyoma’s Luck L is defined as probability of performing a super attack. A super attack increases power of Normal Attack by C. Given this information calculate and print the probability that Kyoma kills Nomu and survives. If Kyoma dies print RIP.

Constraints
0 < T <= 50
1 <= A, H, C, L1, L2 <= 1000
1 <= M <= 20.
L1<=L2
Input Format
First line is integer T denoting number of test cases
Each test case consist of single line with space separated numbers A H L1 L2 M C.
Where luck L is defined as L1/L2. Other numbers are, as described above.
Output
Print probability that Kyoma kills Nomu in form P1/P2 where P1<=P2 and gcd(P1,P2)=1
If impossible, print RIP without quotes.
Example Input 1
2
10 33 7 10 3 2
10 999 7 10 3 2
Output
98/125
RIP

'''

import math

fact = [1,1,2,6,24,120,720,5040,40320,362880,3628800,39916800,479001600,6227020800,87178291200,1307674368000,20922789888000,355687428096000,6402373705728000,121645100408832000,2432902008176640000]

def minus(n1, n2):
    numerator = n1[0]*n2[1] - n2[0]*n1[1]
    denominator = n1[1]*n2[1]

    ans_numerator = numerator//math.gcd(numerator,denominator)
    ans_denominator = denominator//math.gcd(numerator,denominator)

    return [ans_numerator, ans_denominator]

def add(n1,n2):
    numerator = n1[0]*n2[1] + n2[0]*n1[1]
    denominator = n1[1]*n2[1]

    ans_numerator = numerator//math.gcd(numerator,denominator)
    ans_denominator = denominator//math.gcd(numerator,denominator)

    return [ans_numerator, ans_denominator]


def mult(n1,n2):
    numerator = n1[0]*n2[0]
    denominator = n1[1]*n2[1]

    ans_numerator = numerator//math.gcd(numerator,denominator)
    ans_denominator = denominator//math.gcd(numerator,denominator)

    # print('mult',n1,n2,[ans_numerator, ans_denominator])

    return [ans_numerator, ans_denominator]

def exp(n1,k):
    ans = [1,1]
    for i in range(k):
        ans = mult(ans, n1)
    # print('exp',n1,k,ans)
    return ans

def nCr(n,r):
    if n == r or r == 0:
        # print('ncr',n,r,1,1)
        return [1,1]
    if r == 1 or r==n-1:
        # print('ncr',n,r,n,1)
        return[n,1]
    numerator = fact[n]
    denominator = fact[r] * fact[n-r]

    ans_numerator = numerator//math.gcd(numerator,denominator)
    ans_denominator = denominator//math.gcd(numerator,denominator)

    # print('ncr',n,r,ans_numerator,ans_denominator)
    return [ans_numerator, ans_denominator]


T = int(input())

for case in range(T):
    A,H,L1,L2,M,C = list(map(int, input().split()))

    P1,P2 = 0,0

    if (A+C)*M < H:
        print('RIP')
        continue
    if A*M >= H:
        P1,P2 = 1,1
        numerator = P1/(math.gcd(P1,P2))
        denominator = P2/(math.gcd(P1,P2))
        print(f'{numerator}/{denominator}')
        continue
    
    remaining = H - (A*M)
    required_lucky_attacks = math.ceil(remaining/C)

    curr_frac = [0,1]
    prob_lucky = [L1//math.gcd(L1,L2), L2//math.gcd(L1,L2)]
    prob_not_lucky = minus([1,1], prob_lucky)
    # print(prob_lucky, prob_not_lucky)

    for i in range(required_lucky_attacks, M+1):
        curr_prob = mult(nCr(M,i),exp(prob_lucky,i))
        curr_not_prob = exp(prob_not_lucky,M-i)
        curr_prob = mult(curr_prob,curr_not_prob)
        curr_frac = add(curr_frac,curr_prob)
        # print(curr_frac)
        # print('---')

    print(f'{curr_frac[0]}/{curr_frac[1]}')
    


##############################################################################

##OR

'''
from math import gcd,factorial
def ncr(n,r):
    return factorial(n)/(factorial(n-r)*(factorial(r)))
for i in range(int(input())):
    a,h,l1,l2,m,c = [int(i) for i in input().split()]
    num = 0
    den = pow(l2,m)
    if m*(a+c) < h:
        print("RIP")
    else:
        k,z = 0,m*a
        while z < h:
            z += c
            k += 1
        for i in range(k,m+1):
            if i == 0:
                num += pow(l2 - l1,m)
            elif i == m:
                num += pow(l1,i)
            else:
                num += (pow(l1,i)*pow(l2-l1,m-i)*ncr(m,i))
        x = gcd(int(num),den)
        print(str(int(num/x))+"/"+str(int(den/x)))

        '''
