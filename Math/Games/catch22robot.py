'''
Catch 22
A robot is programmed to move forward F meters and backwards again, say B meters, in a straight line. The Robot covers 1 meter in T units of time. On Robot’s path there is a ditch at a distance FD from initial position in forward direction as well as a ditch at a distance BD from initial position in backward direction. This forward and backward movement is performed repeatedly by the Robot.

Your task is to calculate amount of time taken, before the Robot falls in either ditch, if at all it falls in a ditch.

Input Format
First line contains total number of test cases, denoted by N

Next N lines, contain a tuple containing 5 values delimited by space F B T FD BD, where

F denotes forward displacement in meters
B denotes backward displacement in meters
T denotes time taken to cover 1 meter
FD denotes distance from Robot’s starting position and the ditch in forward direction
BD denotes distance from Robot’s starting position and the ditch in backward direction
Output Format
For each test case print time taken by the Robot to fall in the ditch and also state which ditch he falls into. Print F for forward and B for backward. Both the outputs must be delimited by whitespace

OR

Print No Ditch if the Robot does not fall in either ditch

Constraints:
First move will always be in forward direction
1 <= N <= 100000
forward displacement > 0
backward displacement > 0
time > 0
distance of ditch in forward direction (FD) > 0
distance of ditch in backward direction (BD) > 0
All input values must be positive integers only
Sample Input / Output
Input

3
9 4 3 13 10
9 7 1 11 13
4 4 3 8 12

Output

63 F
25 F
No Ditch

Input

5
8 4 7 11 22
4 5 4 25 6
4 9 3 6 29
7 10 6 24 12
10 10 1 9 7

Output

133 F
216 B
231 B
408 B
9 F
'''

from math import inf
def solve(F,B,FD,BD):
    if F>=FD:
        return FD,'F'
    if BD<=B-F:
        return F+F+BD, 'B'
    if B==F:
        return inf, None
    if F-B>0:
        meters=0
        dF=F-B
        distPerStep=F+B
        
        if ((FD-F)%dF)==0:
            numofFullSteps = (FD-F)//dF
            meters+=numofFullSteps * distPerStep +F
        else:
            numofFullSteps = (FD-F)//dF + 1
            remainingDist = FD - numofFullSteps * dF
            meters+=numofFullSteps * distPerStep + remainingDist
        return meters, 'F'
    if B-F>0:
        meters=0
        dB=B-F
        distPerStep=F+B
        
        if ((BD)%dB)==0:
            numofFullSteps = (BD)//dB
            meters+=numofFullSteps * distPerStep
        else:
            numofFullSteps = (BD)//dB + 1
            remainingDist = (numofFullSteps * dB)-BD
            meters+=numofFullSteps * distPerStep - remainingDist
        return meters, 'B'
    

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        F,B,T,FD,BD=[int(x) for x in input().strip().split()]
        dist, direction=solve(F,B,FD,BD)
        time=dist*T
        if time==inf:
            print('No Ditch')
        else:
            print(f"{time} {direction}")
    

