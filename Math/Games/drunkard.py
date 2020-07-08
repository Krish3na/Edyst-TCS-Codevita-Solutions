'''
Drunkard’s Walk
In state of inebriation, a drunkard sets out to walk home, afoot. As is common knowledge, a drunkard struggles to find balance and ends up taking random steps. Not surprisingly these are steps in both forward as well as backward direction. Funnily enough, these are also repeated movements. Now, it so happens that on this drunkard’s path, there are two banana skins - one in forward direction and one in backward direction. There is a real danger that the drunkard’s downfall may be accelerated if he accidentally slips over either of those banana skins.

Your task is to find out if he will slip over the banana skin on forward path or banana skin on backward path and in how much time. It is also possible that by his good fortune he might not step over either banana skins. Write a program to calculate the outcome.

Input Format
First line contains total number of test cases, denoted by N
Next N lines, contain a tuple containing 6 values delimited by space
D FM BM T FBS BBS, where

D denotes direction, either F (Forward) or B (Backward)
FM denotes the magnitude of forward movement in meters
BM denotes the magnitude of backward movement in meters
T denotes time taken to cover 1 meter
FBS denotes distance from Drunkards’ starting position and the banana skin in forward direction
BBS denotes distance from Drunkards’ starting position and the banana skin in backward direction
Output Format
For each test case, print time taken by the Drunkard to slip over the forward or backward banana skin. Print F if he slips over forward banana skin and B if he slips over the backward banana skin. Both the outputs must be delimited by whitespace

OR

Print Hurray if the Drunkard is lucky to not slip over either banana skin

Constraints
1 <= N <= 100
forward movement (FM) > 0
backward movement (BM) > 0
time (T) > 0
Distance to banana skin in forward direction (FBS) > 0
Distance to banana skin in backward direction (BBS) > 0
All input values must be integer only
Sample Input / Output
Input

6
B 14 12 7 25 4
B 11 4 6 10 17
F 2 3 9 12 15
F 1 12 3 22 28
B 8 8 5 9 18
F 8 8 5 7 9

Output

28 B
156 F
675 B
102 B
Hurray
35 Fs

'''


from math import inf
def solve(D,F,B,FB,BB):
    if D=='F':
        if F>=FB:
            return FB,'F'
        if BB<=B-F:
            return F+F+BB, 'B'
        if B==F:
            return inf, None
        if F-B>0:
            meters=0
            dF=F-B
            distPerStep=F+B
        
            if ((FB-F)%dF)==0:
                numofFullSteps = (FB-F)//dF
                meters+=numofFullSteps * distPerStep +F
            else:
                numofFullSteps = (FB-F)//dF + 1
                remainingDist = FB - numofFullSteps * dF
                meters+=numofFullSteps * distPerStep + remainingDist
            return meters, 'F'
        if B-F>0:
            meters=0
            dB=B-F
            distPerStep=F+B
        
            if ((BB)%dB)==0:
                numofFullSteps = (BB)//dB
                meters+=numofFullSteps * distPerStep
            else:
                numofFullSteps = (BB)//dB + 1
                remainingDist = (numofFullSteps * dB)-BB
                meters+=numofFullSteps * distPerStep - remainingDist
            return meters, 'B'
    if D=='B':
        if B>=BB:
            return BB,'B'
        if FB<=F-B:
            return B+B+FB, 'F'
        if B==F:
            return inf, None
        if B-F>0:
            meters=0
            dB=B-F
            distPerStep=F+B
        
            if ((BB-B)%dB)==0:
                numofFullSteps = (BB-B)//dB
                meters+=numofFullSteps * distPerStep + B
            else:
                numofFullSteps = (BB-B)//dB + 1
                remainingDist = BB - numofFullSteps * dB
                meters+=numofFullSteps * distPerStep + remainingDist
            return meters, 'B'
        if F-B>0:
            meters=0
            dF=F-B
            distPerStep=F+B
        
            if ((FB)%dF)==0:
                numofFullSteps = (FB)//dF
                meters+=numofFullSteps * distPerStep
            else:
                numofFullSteps = (FB)//dF+1
                remainingDist = (numofFullSteps * dF)-FB
                meters+=numofFullSteps * distPerStep - remainingDist
            return meters, 'F'
    

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        Lis=input().split()
        F,B,T,FB,BB=[int(x) for x in Lis[1:]]
        D=Lis[0]
        dist,direction=solve(D,F,B,FB,BB)
        time=dist*T
        if time==inf:
            print('Hurray')
        else:
            print(f"{time} {direction}")
