'''
Reverse Gear
A futuristic company is building an autonomous car. The scientists at the company are training the car to perform Reverse parking. To park, the car needs to be able to move in backward as well as forward direction. The car is programmed to move backwards B meters and forwards again, say F meters, in a straight line. The car does this repeatedly until it is able to park or collides with other objects. The car covers 1 meter in T units of time. There is a wall after distance D from car’s initial position in the backward direction.

The car is currently not without defects and hence often hits the wall. The scientists are devising a strategy to prevent this from happening. Your task is to help the scientists by providing them with exact information on amount of time available before the car hits the wall.

Input Format
First line contains total number of test cases, denoted by N
Next N lines, contain a tuple containing 4 values delimited by space
F B T D, where

F denotes forward displacement in meters
B denotes backward displacement in meters
T denotes time taken to cover 1 meter
D denotes distance from Car’s starting position and the wall in backward direction
Output Format
For each test case print time taken by the Car to hit the wall

Constraints
First move will always be in backward direction
1 <= N <= 100
backward displacement > forward displacement i.e. (B > F)
forward displacement (F) > 0
backward displacement (B) > 0
time (T) > 0
distance (D) > 0
All input values must be positive integers only
Sample Input / Output
Input
2
6 9 3 18
3 7 5 20

Output
162
220
'''
from math import inf
def solve(F,B,D):
    if D<=B:
        return D
    if F==B:
        return inf
    if B-F>0:
        meters=0
        dB=B-F
        distPerStep=F+B
        if (D-B)%dB==0:
            numofFullSteps=(D-B)//dB
            meters+= numofFullSteps * distPerStep + B
        else:
            numofFullSteps=(D-B)//dB + 1
            remainingdist = D - (numofFullSteps * dB)
            meters+= numofFullSteps * distPerStep + remainingdist
            
        return meters

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        F,B,T,D = [int(x) for x in input().strip().split()]
        dist=solve(F,B,D)

        time = dist * T
        if time==inf:
            print(-1)
        else:
            print(time)
