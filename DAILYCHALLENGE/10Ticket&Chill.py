'''
Ticket & Chill
Jay works for support project where he has to resolve some tickets each day (denoted by A[i]). He knows, ahead of time, the number of tickets for each day for N days. Let A be an array of length N.

Each element A[i] (where i=1 to i=N) denotes number of tickets to resolve on ith day. Jay is struggling to balance his work life.

On some days, workload is huge and on other days, it is very little. Now he can procrastinate and choose to postpone up to K tickets to next day. However, tickets can only be postponed once. (Refer example 2 for more clarity). Find optimal solution where workload can be distributed as evenly as possible with above constraints and print the maximum number of tickets he needs to resolve on given days.

Constraints
1<= T <= 50
1<= N <= 100
1<= K <= 100
1<= A[i] <= 10^9
Input Format
First line is integer T denoting number of test cases.
For each test case:
First line is N K described above
Next line is N spaced integers denoting number of tickets for each day
Output
For each test case, print a single integer per line denoting maximum number of tickets Jay needs to resolve after optimal rearrangement with above constraints.
Example Input
2
3 100
3 1 2
3 1532
28 31 37
Output
2
37
Explanation
Initially highest workload is on first day (3 tickets). Now 1 ticket should be postponed from day 1 to day 2. So array is [2,2,2] and maximum workload is 2. For second testcase, no rearrangement is required, hence the output is 37.

Example Input
1
3 100
7 1 1
Output:

4
Explanation:

Initially highest workload is on first day (7 tickets). Now we postpone 4 tickets from day 1 to day 2. Array now looks like [3,5,1]. Now on day 2, even K is 100, we can only postpone 1 ticket since tickets can only be postponed once. (In other words, 4 tickets out 5 which were postponed from day 1 has to be resolved on day 2. They cannot be postponed any further). So after postponing 1 ticket array looks like [3,4,2] and maximum workload is 4, hence answer is 4.

'''
###
'''
    This question can be solved using binary search on the maximum possible tickets that can be resolved in a day.
    The lower bound is 1, while the upper bound is the maximum number of tickets on any specific day.
    After obtaining a value for the maximum amount of tickets that can be resolved in a day, we check if there is solution with these
    number of tickets in a day.
    To check if there is a solution, I define a utility function check which takes in 4 parameters: the array a, the maximum number of
    tickets that can be resolved in a day (mx), the maximum number of tickets that can be transferred to the next day(k), and the total
    number of elements in the array(n).
    lst is the number of tickets that we transfer to the next day. If a[i]+lst<=mx, then we can resolve all tickets on that day, and 
    lst is reset to 0.
    Let u = mx-lst, where u is the maximum number of tickets that can be resolved on that same day.
    We can transfer min(a[i]-u,k) tickets to the next day.
    We then check this condition for all days.

'''
def check(a,mx,k,n):
    lst = 0
    for i in range(n):
        if(a[i]+lst<=mx):
            lst = 0
            continue
        if(lst>mx):
            return False
        u = mx-lst
        nlst = min(a[i]-u,k)
        nlst = max(nlst,0)
        if(a[i]-nlst+lst>mx):
            return False
        lst = nlst
    if(lst!=0):
        return False
    return True

T = int(input())
for tc in range(T):
    n,k = map(int,input().strip().split())
    lo = 1
    a = list(map(int,input().strip().split()))
    hi = max(a)
    best = hi
    while(lo<=hi):
        mid = (lo+hi)//2
        if(check(a,mid,k,n)):
            best = mid
            hi = mid-1
        else:
            lo = mid+1
    print(best)
################################################################

##OR
'''
t=int(input())

for _ in range(t):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    for i in range(1,n):
        if(a[i-1]<a[i]):
            continue
        else:
            count=1
            while((a[i-1]>a[i]) & (count<=k)):
                a[i]+=1
                a[i-1]-=1
                count+=1
    print(max(a))

'''
