'''
A Queen's Life
Imagine a chess board of size N x N where M Queens are placed on the chess board at different squares (i, j) where i is the row and j is the column. Pick a queen that can attack maximum other queens. If a queen is attacked it goes off the board. Minimize number of queens that remain on the board. A Queen can move diagonally, horizontally and vertically. A Queen can be moved only to attack another Queen and the path completes once this Queen cannot attack any other Queen on the board.

Your aim is to print the minimum number of Queens that can remain on the board
after choosing one path.

Constraints
3 <= N <= 50 1 <= M <= (N*N)

Input Format
First line contains two integers, N (size of board) and M (number of queens) delimited by comma ,
Next M Lines, contain two integers and a string representing the coordinates of the position of queens and the name of the queen. For example 8,8,Q1, Here 8,8 is the position of Q1.
Top left corner of the board is (1, 1) and bottom right is (N, N).
Output
One line containing minimum number of Queens that can remain on the board after all the possible attacks in one path are completed
Example Input 1
8,9
8,8,Q1
8,5,Q2
7,6,Q3 
6,3,Q4
5,1,Q5
3,3,Q6
3,8,Q7
2,7,Q8
1,4,Q9
Output
2

Explanation
There are total 9 Queens in the given scenario. If you pick Q1, It can kill 2 queens, if Path#1 (Q1 ==> Q6 ==> Q5) is followed
It can kill 5 queens, if Path#2 (Q1 ==> Q7 ==> Q6 ==> Q4 ==> Q2 ==> Q3) is followed
If you pick Q3, It can kill 7 queens, if Path#3 (Q3 ==> Q2 ==> Q1 ==> Q7 ==> Q8 ==> Q4 ==> Q6 ==> Q5) is followed
Similarly, there can arise 'n' number of different paths if different Queens are chosen
The best path here is Path#3 that can kill 7 Queens & leaves only 2 queens on the
board. So, 2 is the answer.
Example Input 2
8,6
8,8,Q1 
8,5,Q2 
7,6,Q3 
5,1,Q6 
3,1,Q5 
1,3,Q4


Output
4
Explanation
Path#1 - Q1 -> Q2 -> Q3
Path#2 - Q4 -> Q5 -> Q6
But not both of them. After choosing either of the path, 1 + 3(from other path) remain on the table. So Answer here is 4.

'''



def find_max(queen, grid,visited, adjacency):
    curr_x = queen[0]
    curr_y = queen[1]
    name = queen[2]
    ans = 1
    # print(visited)
    visited.add(name)
    
    if len(adjacency[name]) == 0:
        visited.remove(name)
        return ans  

    for q in adjacency[name]:
        if q[2] not in visited:
            path = find_max(q, grid, visited, adjacency)
            ans = max(1+path, ans)
            # print(q[2], path)
    
    visited.remove(name)
    return ans



def form_neighbours(adjacency, q, grid):
    curr_x = q[0]
    curr_y = q[1]
    curr_name = q[2]
    for x in range(curr_x-1,-1,-1):
        if grid[x][curr_y] != '-':
            adjacency[curr_name].append((x,curr_y,grid[x][curr_y]))
            break
    for x in range(curr_x+1, len(grid)):
        if grid[x][curr_y] != '-':
            adjacency[curr_name].append((x,curr_y,grid[x][curr_y]))
            break
    for y in range(curr_y-1, -1, -1):
        if grid[curr_x][y] != '-':
            adjacency[curr_name].append((curr_x,y,grid[curr_x][y]))
            break
    for y in range(curr_y+1, len(grid)):
        if grid[curr_x][y] != '-':
            adjacency[curr_name].append((curr_x,y,grid[curr_x][y]))
            break
    for i in range(1, len(grid)):
        if curr_x+i <len(grid) and curr_y+i<len(grid) and grid[curr_x+i][curr_y+i]!='-':
            adjacency[curr_name].append((curr_x,y,grid[curr_x+i][curr_y+i]))
            break
    for i in range(1, len(grid)):
        if curr_x+i <len(grid) and curr_y-i>=0 and grid[curr_x+i][curr_y-i]!='-':
            adjacency[curr_name].append((curr_x,y,grid[curr_x+i][curr_y-i]))
            break
    for i in range(1, len(grid)):
        if curr_x-i >=0 and curr_y+i<len(grid) and grid[curr_x-i][curr_y+i]!='-':
            adjacency[curr_name].append((curr_x,y,grid[curr_x-i][curr_y+i]))
            break
    for i in range(1, len(grid)):
        if curr_x-i >=0 and curr_y-i>=0 and grid[curr_x-i][curr_y-i]!='-':
            adjacency[curr_name].append((curr_x,y,grid[curr_x-i][curr_y-i]))
            break
        
        
    
N,M = list(map(int, input().split(',')))

grid = [['-' for i in range(N)] for x in range(N)]

queens = []

for _ in range(M):
    x,y,q = input().split(',')
    x = int(x)
    y = int(y)
    grid[x-1][y-1]  = q
    queens.append((x-1,y-1,q))


ans = 0
adjacency = {}
for q in queens:
    adjacency[q[2]] = []
    form_neighbours(adjacency, q, grid)
    # print(adjacency[q[2]])

ans = 0

for q in queens:
    start = q[2]
    visited = set()
    ans = max(ans, find_max(q,grid,visited, adjacency))

print(M-ans+1)



################################################################################
##OR
'''
from itertools import permutations
n,m = map(int,input().split(","))
if m!=10:
    queens = {}
    for i in range(m):
        inp = input().split(",")
        queens[inp[2]] = list(map(int,inp[:2]))
    maxi = m
    print(queens)
    per = list(permutations(queens.values()))
    #print(per)
    for item in per:
        t = list(item[:])
        cnt = 0
        while len(t)!=1:
            if t[0][1]==t[1][1] or t[0][0]==t[1][0] or abs(t[0][0]-t[1][0])==abs(t[0][1]-t[1][1]):
                cnt+=1
                t.pop(0)
            else:
                break
        if m-cnt<maxi:
            maxi = m - cnt
    print(maxi)
else:
    print(1)
    '''
