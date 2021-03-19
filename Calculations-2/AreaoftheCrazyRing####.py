'''

Area of the Crazy Ring
Scientists have found a strange substance having strange properties. There is one triangular substance called Strange Triangle which has a property that if it is placed inside a circle, then it contracts/shrinks the circle until all the corners of the triangle are touching the circle. There is another circular substance called Strange Circle, which when placed inside any polygon, expands such that it becomes the largest possible circle which can fit inside the polygon such that it touches every side of the polygon.

Now researchers did a strange experiment. They placed a Strange Triangle inside a normal circle and then placed a Strange Circle inside this Strange Triangle. Thus the ring formed by the two circles, the normal outer circle and the inner strange circle is named Crazy Ring. You are provided with the coordinates of the Strange Triangle on coordinate plane and you have to calculate the area of the Crazy Ring formed by the structure, Print “Not Possible” if the ring is not possible to form.

Input Format:
The first line contains k, the number of inputs. The following k lines contain:

First line contains two space delimited numbers N1 M1 (N1 and M1 can also be negative)
Second line contains two space delimited numbers N2 M2 (N2 and M2 can also be negative)
Third line contains two space delimited numbers N3 M3 (N3 and M3 can also be negative)
Where, (N1, M1) , (N2, M2) and (N3, M3) are x and y coordinates of three points representing the Strange Triangle

Output Format:
Output the area of the crazy ring up to 2 decimal places however calculations are to be performed up to a precision of 11 decimal places

OR

Print “Not Possible” if it is not possible to form the ring

Sample Input and Output
Input 1:

3
5 5
5 20
20 5
Output:

292.79
Input 2:

3
5 5
5 5
5 5
Output:

Not Possible
Input 3:

3
5 8
4 3
2 4.34534554521
Output:

17.91

'''

import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def isTriangleValid(a, b, c):
    if a+b>c and b+c>a and c+a>b:
        return True
    return False

def circumcircleRadius(a, b, c):
    return float((a * b * c) /(math.sqrt((a + b + c) * (b + c - a) * (c + a - b) * (a + b - c))))

def incircleRadius(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(((s - a) * (s - b) * (s - c)) / (s))

def solve(x1, y1, x2, y2, x3, y3):
    # calculate side lengths like below:
    a = dist(x1, y1, x2, y2)
    b = dist(x3, y3, x2, y2)
    c = dist(x1, y1, x3, y3)

    # check that a, b, c form a valid triangle
    if isTriangleValid(a, b, c):

        circumcircle_radius = circumcircleRadius(a, b, c)
        incircle_radius = incircleRadius(a, b, c)

        area_of_ring = math.pi*circumcircle_radius*circumcircle_radius - math.pi*incircle_radius*incircle_radius
        if circumcircle_radius >0.0 and incircle_radius>0.0:
            print('{:.2f}'.format(area_of_ring)) 
        else:
            print("Not Possible")
    
    else:
        print("Not Possible")

k=int(input())
for i in range(k//3):
    x1,y1=map(float,input().split())
    x2,y2=map(float,input().split())
    x3,y3=map(float,input().split())


    solve(x1,y1,x2,y2,x3,y3)

'''

Area of Crazy Ring [EDITORIAL]
This question requires you to have two things:

A piece of paper, and a pen/pencil
Very basic understanding of geometry
When you place a strange circle inside a triangle, what does it look like? According to the question, it moves and expands to touch all sides, and if you draw it out, this is what it’ll look like.

./area_crazy3.png

Now, what if you put a strange triangle inside a circle? It’ll contract and move the outer circle till all three points of the triangle are touching the circle. This situation looks like this:

./area_crazy2.png

Coming back to the original question, when we place a strange triangle inside a circle, and a strange circle inside that strange triangle, this is how they will arrange themselves:

./area_crazy1.png

If you notice both circles carefully, they are nothing but the Incircle and the Circumcircle of the triangle! this is where familiarity with both of these geometric concepts helps to solve this question 😄

After that, all that remains is to quickly search the formula of calculating the radius of the incircle and the circumcircle given the side lengths of the triangle. Once you have the formulae (look at the pseudo-code below), you need to calculate the areas of the two circles and subtract them to get the area of the ring!

Here is a good way to structure your program.

Note that this code will NOT run/compile as is. It is designed to give you an idea of how to approach the problem and structure your solution!

def dist(x1, y1, x2, y2):
    return distance between 2 points (x1, y1) and (x2, y2)
 
def isTriangleValid(a, b, c):
    return True/False given side lengths a, b, c 
        depending on whether a triangle can exist with those sides
 
def circumcircleRadius(a, b, c):
    return (a * b * c) / sqrt(
        (a + b + c) * (b + c - a) * (c + a - b) * (a + b - c)
    )
 
def incircleRadius(a, b, c):
    s = (a + b + c) / 2
    return sqrt((s - a) * (s - b) * (s - c) / s)
 
def solve(x1, y1, x2, y2, x3, y3):
    # calculate side lengths like below:
    a = dist(x1, y1, x2, y2)
    b = dist(x3, y3, x2, y2)
    c = dist(x1, y1, x3, y3)
 
    # check that a, b, c form a valid triangle
    if isTriangleValid(a, b, c):
 
        circumcircle_radius = circumcircleRadius(a, b, c)
        incircle_radius = incircleRadius(a, b, c)
 
        area_of_ring = difference in areas of both circles
Take care to print the area to as many digits after the decimal point as demanded by the question!

'''
