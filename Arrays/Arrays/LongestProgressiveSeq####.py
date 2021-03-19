'''
Longest Progressive Sequence
Longest Progressive Sequence
Given a sequence, the objective is to find the longest progressive sequence arranged in ascending order. Detailed descriptions are as:

A sequence is said to be progressive if it doesn’t decrease at any point in time.
For example 1 1 2 2 is a progressive sequence but 1 2 1 is not a progressive sequence. Let S be the sequence and be represented by T spaced integers Ki, now your task is to find out the first longest progressive sequence present in the given sequence (S).

Input Format:
First line will contain N, the number of test cases. After than 2*N lines follow.

For each test case, the first line will contain T, the length of the sequence and next line will contain T spaced integers Ki (where i = 0,1, ...,L).

Line 1 T,where T is the length of the sequence
Line 2 Ki,where Ki is integer in sequence separated by space
Constraints:
1<=T<=10^6 (one million)
-10^9<=Ki<=10^9 (one billion)
Output Format:
Line 1 longest progressive sequence present in the given sequence
If more than 1 sequence exists, then print the one whose starting index is least, i.e., the one that comes first.

Sample Test Cases:
Input:

1
4
1 1 2 1
Output:

1 1 2
Input:

1
5
1 2 1 2 2
Output:

1 2 2

'''
################# Some test  cases may fail
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().strip().split()))
    
    assert len(l)==n
    
    start,end=0,1
    max_start,max_end=0,1
        
    
    for i in range(1,n):
        if l[i]>=l[i-1]:
            end = i
            if end-start > max_end-max_start:
                max_start,max_end = start,end
                #print(max_start,max_end)
        else:
            start = i
            end = i + 1
            
    for i in range(max_start,max_end+1):
        print(l[i],end=' ')
    print()


###############################################################################

##########  Effective Solution   
def solve(S):
    # longest progressive subsequence from [K_si ... K_sj)
    #   i.e. K_sj not included
    si = 0
    sj = 1

    # current subsequence indices [i,j)
    i = 0
    j = 1
    while i < j < len(S):
        # while the subsequence is increasing, increment j
        while j < len(S) and S[j] >= S[j - 1]:
            j += 1
        # subsequence ends here, if current subsequence is strictly longer than
        #   our current longest subseq [si, sj), update it
        if j - i > sj - si:
            si, sj = i, j
        # prepare new subsequence
        i = j
        j = j + 1

    # return a space separated string represntation of the subsequence
    return " ".join(map(str, S[si:sj]))


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        T = int(input())
        S = list(map(int, input().strip().split()))

        assert len(S) == T

        print(solve(S))
