'''
Some prime numbers can be expressed as Sum of other consecutive prime numbers.
For example

5 = 2 + 3
17 = 2 + 3 + 5 + 7
41 = 2 + 3 + 5 + 7 + 11 + 13
Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N subject to a constraint that summation should always start with number 2.

Write code to find out number of prime numbers that satisfy the above mentioned property in a given range.

Input Format:
First line of input contains k - the number of inputs
The next k lines contains a number N.

Output Format:
Print the total number of all such prime numbers which are less than or equal to N.

Example:
Input:
k = 2
 
N = 20
 
N = 15
Output:
2 (there are 2 such numbers: 5 and 17)
1
'''

'''
def isprime(n):
    isprime=True
    if n<=1:
        isprime=False
    for i in range(2,n):
        if n%i==0:
            isprime=False
            break
    return isprime
'''
def SieveOfEratosthenes(n):      
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Append all prime numbers
    primelist=[]
    for p in range(n + 1): 
        if prime[p]:
            primelist.append(p)
    return primelist

def consecutiveprimes(n):
    plist=SieveOfEratosthenes(n)
    if n==1 or n==2:
        return 0
    
    count=0 
    for i in range(1,len(plist)):
        sum=0
        for j in plist:
            sum+= j
            if sum==plist[i]:
                count+=1
            elif sum>=plist[i]:
                break
    return count

t=int(input())
for i in range(t):
    n=int(input())
    print(consecutiveprimes(n))
