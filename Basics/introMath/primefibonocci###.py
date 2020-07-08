'''
Prime Fibonacci Combinations
Given two numbers n1 and n2

Find prime numbers between n1 and n2, then
Make all possible unique combinations of numbers from the prime numbers list you found in step 1.
From this new list, again find all prime numbers.
Find smallest a and largest b number from the 2nd generated list, also count of this list.
Consider smallest and largest number as the 1st and 2nd number to generate Fibonacci series respectively till the count (number of primes in the 2nd list).
Print the last number of a Fibonacci series as an output
Input Format
First line contains T, the number of test cases. Each test case contains:
One line containing two space separated integers n1 and n2.
Output
Last number of a generated Fibonacci series.
Constraints
1 <= T <= 2
2 <= n1, n2 <= 100
n2 - n1 >= 35
Example Input 1
1
2 40
Output
13158006689
Explanation
1st prime list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
Combination of all the primes = [23, 25, 27, 211, 213, 217, 219, 223, 229, 231, 32, 35, 37, 311, 313, 319, 323, 329, 331, 337, 52, 53, 57, 511, 513, 517, 519, 523, 529, 531, 537, 72, 73, 75, 711, 713, 717, 719, 723, 729, 731, 737, 112, 113, 115, 117, 1113, 1117, 1119, 1123, 1129, 1131, 1137, 132, 133, 135, 137, 1311, 1317, 1319, 1323, 1329, 1331, 1337, 172, 173, 175, 177, 1711, 1713, 1719, 1723, 1729, 1731, 1737, 192, 193, 195, 197, 1911, 1913, 1917, 1923, 1929, 1931, 1937, 232, 233, 235, 237, 2311, 2313, 2317, 2319, 2329, 2331, 2337, 292, 293, 295, 297, 2911, 2913, 2917, 2919, 2923, 2931, 2937, 312, 315, 317, 3111, 3113, 3117, 3119, 3123, 3129, 3137, 372, 373, 375, 377, 3711, 3713, 3717, 3719, 3723, 3729, 3731]
2nd prime list = [193, 3137, 197, 2311, 3719, 73, 137, 331, 523, 1931, 719, 337, 211, 23, 1117, 223, 1123, 229, 37, 293, 2917, 1319, 1129, 233, 173, 3119, 113, 53, 373, 311, 313, 1913, 1723, 317]
smallest (a) = 23
largest (b) = 3719
Therefore, the last number of a Fibonacci series i.e. 34th Fibonacci number in the series that has 23 and 3719 as the first 2 numbers is 13158006689
Example Input 2
1
30 70
Output
2027041
Explanation
1st prime list = [31, 37, 41, 43, 47, 53, 59, 61, 67]
2nd prime list generated form combination of 1st prime list = [3137, 5953, 5347, 6761, 3761, 4337, 6737, 6131, 3767, 4759, 4153, 3167, 4159, 6143]
smallest prime in 2nd list = 3137
largest prime in 2nd list = 6761
Therefore, the last number of a Fibonacci series i.e. 14th Fibonacci number in the series that has 3137 and 6761 as the first 2 numbers is 2027041
'''

def get_primes(start,end):
    primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    
    start_idx=0
    end_idx=len(primes)-1
    
    while(start_idx<=end_idx and primes[start_idx]<start):
        start_idx+=1
    while(start_idx<=end_idx and primes[end_idx]>end):
        end_idx-=1
        
    req_list=primes[start_idx:end_idx+1]
    return req_list

def combinations(primelist):
    combinations_list=[]
    for i in range(len(primelist)):
        for j in range(len(primelist)):
            if i!=j:
                combined=int(str(primelist[i])+str(primelist[j]))
                if isprime(combined):
                    combinations_list.append(combined)
    combinations_list=list(set(combinations_list))
    return combinations_list

def isprime(n):
    if n<=1:
        return False
    if n%2==0:
        return False
    i=2
    while(i*i<=n):
        if n%i==0:
            return False
        i+=1
    return True

def fibonocci_num(first,second,n):
    if n==1:
        return first
    if n==2:
        return second
    for i in range(3,n+1):
        ans=first+second
        first=second
        second=ans
    return ans


t=int(input())
for i in range(t):
    start, end =map(int,input().split())
    primes=get_primes(start,end)
    combinations_list=combinations(primes)
    smallest_a=min(combinations_list)
    largest_b=max(combinations_list)
    fibo_num=fibonocci_num(smallest_a,largest_b,len(combinations_list))
    print(fibo_num)
    
