'''

CodeVita 2018, Bank Compare
Bank Compare
There are two banks; Bank A and Bank B. Their interest rates vary. You have received offers from both bank in terms of annual rate of interest, tenure and variations of rate of interest over the entire tenure.

You have to choose the offer which costs you least interest and reject the other. Do the computation and make a wise choice.

The loan repayment happens at a monthly frequency and Equated Monthly Installment (EMI) is calculated using the formula given below :

EMI = 
            (loanAmount * monthlyInterestRate)
_________________________________________________________
( 1 - 1 / (1 + monthlyInterestRate)^(numberOfYears * 12))
Input Format
Initially, take input k - the number of test cases. Following k lines include:
First line: P – principal (Loan Amount)
Second line: T – Total Tenure (in years)
Third Line: N1 is number of slabs of interest rates for a given period by Bank A. First slab starts from first year and second slab starts from end of first slab and so on.
Next N1 line will contain the interest rate and their period
After N1 lines we will receive N2 viz. the number of slabs offered by second bank.
Next N2 lines are number of slabs of interest rates for a given period by Bank B. First slab starts from first year and second slab starts from end of first slab and so on.
The period and rate will be delimited by single white space.

Output
Your decision – either Bank A or Bank B.

Constraints
1 <= P <= 1000000
1 <=T <= 50
1<= N1 <= 30
1<= N2 <= 30
Example:
Input:
k = 2
 
10000
20
3
5 9.5
10 9.6
5 8.5
3
10 6.9
5 8.5
5 7.9
 
 
500000
26
3
13 9.5
3 6.9
10 5.6
3
14 8.5
6 7.4
6 9.6
Output:
Bank B
Bank A

'''


def interest(P,t,r):
    EMI=(P*r)//(1+(1//(r**(t*2))))
    return EMI

def solve(P,T,s1,slabPI1,s2,slabPI2):
    total1=0
    for s in slabPI1:
        total1+=interest(P,s[0],s[1])
    #print(total1)
    total2=0
    for s in slabPI2:
        total2+=interest(P,s[0],s[1])
    #print(total2)
    if total1>total2:
        print('Bank B')
    else:
        print('Bank A')


k=int(input())
for i in range(k):
    P=int(input())
    T=int(input())
    s1=int(input())
    slabPI1=[]
    for j in range(s1):
        a=list(input().strip().split())
        a[0]=int(a[0])
        a[1]=float(a[1])
        slabPI1.append(a)
    s2=int(input())
    slabPI2=[]
    for j in range(s2):
        a=list(input().strip().split())
        a[0]=int(a[0])
        a[1]=float(a[1])
        slabPI2.append(a)
    solve(P,T,s1,slabPI1,s2,slabPI2)    
    #print(P,T,s1,s2)
    #print(slabPI1,slabPI2)

