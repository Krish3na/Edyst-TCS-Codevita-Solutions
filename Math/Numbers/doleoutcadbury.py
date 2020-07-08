'''
Dole Out Cadbury
You are a teacher in reputed school. During Celebration Day you were assigned a task to distribute Cadbury such that maximum children get the chocolate. You have a box full of Cadbury with different width and height. You can only distribute largest square shape Cadbury. So if you have a Cadbury of length 10 and width 5, then you need to break Cadbury in 5 x 5 square and distribute to first child and then remaining 5 x 5 to next in queue

Input Format
First line contains T, the number of test cases. In each test case, we have:
4 Space-separated integers P, Q, R and S
P  denotes minimum length of Cadbury in the box,  Q denotes maximum length of Cadbury in the box, R denotes minimum width of Cadbury in the box, S denotes maximum width of Cadbury in the box

Constraints
0 < T < 5
0<P<Q<1501
0<R<S<1501
Output
Print total number of children who will get chocolate.

Example Test Case #1
Input
2
5 7 3 4
1 3 10 12
Output
24
Explanation
Length is in between 5 to 7 and width is in between 3 to 4.
So we have 5 x 3, 5 x 4, 6 x 3, 6 x 4, 7 x 3, 7 x 4 type of Cadbury in the box.
If we take 5 x 3:

First, we can give 3 x 3 square Cadbury to 1st child .Then we are left with 3 x 2. Now largest square is 2 x 2 which will be given to next child. Next, we are left with two  1 x 1 part of Cadbury which will be given to another two children.

And so on...
'''

#dp={}
def count_for(a,b):
    min_side=min(a,b)
    max_side=max(a,b)
    ''' #if range is so big store values 
    curr_pair=(max_side,min_side)
    if curr_pair in dp:
        return dp[curr_pair]
    '''
    if min_side==0:
        return 0
    
    if min_side==1:
        return a*b
    
    total= max_side//min_side
    new_side= max_side % min_side
    total = total + count_for(new_side, min_side)
    
    #dp[curr_pair]=total
    
    return total

t=int(input())
for i in range(t):
    p,q,r,s=map(int,input().split())
    
    ans=0
    
    for i in range(p,q+1):
        for j in range(r,s+1):
            ans = ans + count_for(i,j)
            
    print(ans)
   
