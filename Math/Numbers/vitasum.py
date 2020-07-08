'''
CodeVita 2016, The Vita Sum
The Vita Sum
Tom the cat is brushing up his Math skills. He has a bag containing N balls of different colors. Now Tom can randomly pick any even number of balls from the bag. Tom wants to find out the sum of all such combinations of balls that he can pull out from the bag. He can pull out at max K balls in one pick.

Input Format:
First line contains two space separated numbers N and K

Output Format:
The output is the sum of all the combinations of balls he can pull out modulo 10^9+7 i.e. (1000000007)

Constraints:
0<=N<=10^14
0<=k<=10^6
N >= k
Sample Input and Output
Input
4 4

Output
8

Explanation
We need
4C0 + 4C2+ 4C4= 1+6+1=8

Input
8 3

Output
29

Explanation
We need 8C0 + 8C2= 1+28=29
'''

def solve(n,k,p):
    binsum=0
    if n < 1e6:
        # pre-compute factorials and inverses
        facts, invfacts = fermat_compute(n, p)
        for i in range(0,k+1,2):
            binsum+=binom_precomputed(facts,invfacts,n,i,p)
            binsum%=p
    else:
        for i in range(0,k+1,2):
            binsum+=fermat_binom(n,i,p)
            binsum%=p
        
    return binsum
    
# Using Fermat's little theorem to compute nCk mod p
# Note: p must be prime and k < p
# calculate numerator
# calculate denominator
# numerator * denominator^(p-2) (mod p)
def fermat_binom(n, k, p):
    if n<k:
        return 0
    num = 1
    for i in range(n, n - k, -1):
        num = (num * i) % p
 
    denom = 1
    for i in range(1, k + 1):
        denom = (denom * i) % p
        
    return (num * pow(denom,p-2,p))%p

# Using Fermat's little theorem to pre-compute factorials and inverses
# Note: only works when p is prime and k < p
def fermat_compute(n,p):
    facts=[0]*(n+1)
    invfacts=[0]*(n+1)
    facts[0],invfacts[0]=1,1
    for i in range(1,n+1):
        # calculate factorial and corresponding inverse 
        facts[i]=(facts[i-1]*i)%p
        invfacts[i]=pow(facts[i],p-2,p)
    return facts, invfacts

# Compute binomial coefficient from given pre-computed factorials and inverses
def binom_precomputed(facts, invfacts, n, k, p):
    # n! / (k!^(p-2) * (n-k)!^(p-2)) (mod p)
    return (facts[n]*((invfacts[k]*invfacts[n-k])%p))%p

if __name__=="__main__":
    n,k = map(int,input().split())
    p=int(1e9+7)
    
    print(solve(n,k,p))
