'''

Road Rash
On a busy road, multiple cars are passing by. A simulation is run to see what happens if brakes fail for all cars on the road. The only way for them to be safe is if they don't collide and pass by each other. The goal is to identify whether any of the given cars would collide or pass by each other safely around a Roundabout. Think of this as a reference point O ( Origin with coordinates (0,0) ), but instead of going around it, cars pass through it.

Considering that each car is moving in a straight line towards the origin with individual uniform speed. Cars will continue to travel in that same straight line even after crossing origin. Calculate the number of collisions that will happen in such a scenario.

Calculate collisions only at origin. Ignore the other collisions. Assume that each car continues on its respective path even after the collision without change of direction or speed for an infinite distance.

Constraints
1<=C<=10^5
-10^9 <= x,y <= 10^9
0 < v < 10^9.
Input Format
The first line contains an integer C, denoting the number of cars being considered that are passing by around the origin.
Next C lines contain 3 space delimited values, first two of them being for position coordinates (x,y) in 2D space and the third one for speed (v).
Output
A single integer Q denoting the number of collisions at origin possible for given set of cars.
Example Input 1
5
5 12 1
16 63 5
-10 24 2
7 24 2
-24 7 2
Output
4
Explanation
Let the 5 cars be A, B, C, D, and E respectively.

4 Collisions are as follows -

A & B
A & C
B & C
D & E

'''

n=int(input())
times=[]
for i in range(n):
    x,y,velocity=map(int,input().strip().split())
    distance=((x*x)+(y*y))**(0.5)
    time=distance/velocity
    times.append(time)
collisions=0   
for t in range(n):
    individual_collisions=times[t+1:].count(times[t])
    collisions += individual_collisions
print(collisions)
    
