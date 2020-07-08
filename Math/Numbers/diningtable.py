'''
[CodeVita 2019] Dining Table
In a conference, attendees are invited for a dinner after the conference. The Coordinator, Sagar arranged round tables for dinner and want to have an impactful seating experience for the attendees. Before finalizing the seating arrangement, he want to analyze all possible arrangements. There are R round tables and N attendees. In case where N is an exact multiple of R, the number of attendees must be exactly N/R. If N is not an exact multiple of R, then the distribution of attendees must be as equal as possible. Please refer Example section for better understanding.

For example, R =2 and N=3

All possible seating arrangements are
(1,2) & (3)
(1,3) & (2)
(2,3) & (1)

Attendees are numbered from 1 to N.

Constraints
0 < R <= 10 (Integer)
0 < N <= 20 (Integer)

Input Format
The first line contains T the number of test cases
Each test case contains two space delimited integers R and N, where R denotes the number of round tables and N denotes the number of attendees
Output
Single integer S denoting number of possible unique arrangements

Example Input
1
2 5
Output
10
Explanation
R=2, N=5

(1,2,3) & (4,5)
(1,2,4) & (3,5)
(1,2,5) & (3,4)
(1,3,4) & (2,5)
(1,3,5) & (2,4)
(1,4,5) & (2,3)
(2,3,4) & (1,5)
(2,3,5) & (1,4)
(2,4,5) & (1,3)
(3,4,5) & (1,2)
Arrangements like
(1,2,3) & (4,5)
(2,1,3) & (4,5)
(2,3,1) & (4,5), etc.

But, as it is a round table, all the above arrangements are same
'''


def fact(n):
    ''' #if range in constraints is small hard  coding is best....reduces time computaion
    f=[1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800,
     39916800, 479001600, 6227020800, 87178291200, 1307674368000,
     20922789888000, 355687428096000, 6402373705728000, 121645100408832000,
     2432902008176640000]

     l=[]
     for i in range(1,21):
        l.append(fact(i))
     print(l)
     '''
    f=1
    for i in range(1,n+1):
        f*=i
    return f #f[n-1]

def ncr(n,r):
    if (n==r) or (r==0):
        return 1
    if r==1 :
        return n
    result = fact(n)//fact(r)
    result = result//fact(n-r)
    return result

t=int(input())
for i in range(t):
    r,n=map(int,input().split())
    
    initial=n//r
    extra=n%r
    
    type1=initial+1 #no.of ppl in type1 table
    type2=initial   #no.of ppl in type2 table
    
    combinations=1
    
    for i in range(0,extra):
        combinations = combinations * ncr(n,type1)
        n=n-type1
        
    for i in range(extra,r):
        combinations = combinations * ncr(n,type2)
        n=n-type2
        
    print(combinations)
        
