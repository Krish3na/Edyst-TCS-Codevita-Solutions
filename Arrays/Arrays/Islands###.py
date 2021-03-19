'''
Islands
In the Indian Ocean, there are several small islands. A warship is stationed in the ocean and wants to find how many of these islands are within its striking power. For simplicity, the islands are all assumed to have square shapes and again, the curvature of the earth can be ignored.

The coordinates of two opposite corners of the islands are given and the position of the ship is also given. You need to find the islands in the increasing sequence of their distances from the ship.

The distance is the shortest distance – the distance of the nearest point on the island boundary from the ship. Use Manhattan Distance, i.e. distance between 2 points (x1,y1) and (x2,y2) is |x1-x2| + |y1-y2|.

Constraints
1 <= N <= 105
-109 <= x1i, y1i, x2i,y2i <= 109
Input Format
First line contains single integer N denoting the number of islands.
Next N lines contain 4 integers separated by space denoting the coordinates of the opposite corners of the islands (x1i, y1i) & (x2i,y2i). (1 <= i <= N)
Islands are numbered 1, 2, …, N
The final line contains 2 integer separated by space denoting the coordinates of the warship
Output
N integers separated by space each integer denoting the index of island sorted by distance from warship in non-decreasing order
If 2 islands are at the same distance from warship, rank them according to their index.
Example 1
2
0 0 1 1
0 3 1 4
0 0
Output
1 2
Example 2
3
1 1 0 0
1 2 2 3
3 0 4 1
0 4
Output
2 1 3


'''
def manhattan(x,y,a,b):
    man_distance = abs(x-a) + abs(y-b)
    return man_distance

def distance_from_warship(island,a,b):
    '''when two opposite vertices of a square are given
    other two can be found by following formula (shortcut)
    [x,y]=[((x1+x2)+/-(y1-y2))/2 , ((y1+y2)-/+(x1-x2))/2]'''
    x1,y1=island['x1'],island['y1']
    x2,y2=island['x2'],island['y2']
    x3,y3=((x1+x2)+(y1-y2))/2 , ((y1+y2)-(x1-x2))/2
    x4,y4=((x1+x2)-(y1-y2))/2 , ((y1+y2)+(x1-x2))/2  
    distance=min(manhattan(x1,y1,a,b),manhattan(x2,y2,a,b),manhattan(x3,y3,a,b),manhattan(x4,y4,a,b))
    
    return (distance,island['index'])

n=int(input())
islands=[]
for index in range(n):
    x1,y1,x2,y2=map(int,input().split())
    curr_island={'x1':x1,
                'y1':y1,
                'x2':x2,
                'y2':y2,
                'index':index+1}
    islands.append(curr_island)
a,b=map(int,input().split())

islands.sort(key= lambda x:distance_from_warship(x,a,b))
#print(islands)

for island in islands:
    print(island['index'],end=' ')
