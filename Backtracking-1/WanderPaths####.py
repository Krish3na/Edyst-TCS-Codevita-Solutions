'''

Wander Paths


The city of Looneywalks has a rectangular grid of roads. One of the favorite pastimes of the folks at Looneywalks is to wander around the blocks. While they could take the shortest path, more often, they retrace their steps and engage themselves in finding the number of ways of reaching the destination with a given number of steps. For example, in the figure above a block is shown with 8 blocks and roads around them.

Any walk is a series of symbols U, R, L, D where by U we mean moving one block towards north, R, moving one block East, L moving one block West and D moving one block South. One such path for the above reaching the upper right corner from lower left corner is RRRRUU. This path has length 6 (the number of symbols in the path), which is the shortest path (that do not go outside the grid) between the two points.

If we enumerate all such shortest paths of length 6, there are 15 of them.

Consider a path of length 8: RRLRRRUU. Note that while walking, one cannot move out of the grid. If all the valid paths of length 8 are enumerated, there are 252 of them. However, it soon becomes difficult to enumerate path manually, and we need to use a program. You are given the layout of the roads at Looneywalks. Given a starting point, S ending point E and the length k of the path, write a program to find the number of valid paths from S to E that have length precisely k.

A valid path is one that does not go outside the grid, and two path is one. Every grid point is referred to by the X coordinate and a Y coordinate (the number of blocks east of the southwest corner, and the number of blocks north of the southwest corner). Thus the lower left corner in the above diagram is (0,0) and the top right corner is (4,2).The size of the block is given by two numbers, M and N. M is the number of rows in the grid, and N is the number of columns (in the grid above, M is 2 and N is 4).

Constraints
M, N < 10, k < 20

Input Format
The first line of the input has three comma separated integers M, N and k. The Dimensions of the grid are M blocks in rows, and N blocks in columns. The path length is given by k. The next line has four comma separated numbers giving the coordinates of the starting point and the ending point respectively.

Output
One integer representing the number of valid paths from the starting point to ending point that have length precisely k.

Example Input 1
2,4,6
0,0,4,2
#
Output
15
Explanation
M is 2, and N is 4.

The value of k is 6, and we are counting paths of length 6. The starting point is (0,0) and the end point is (4,2).

The sketch of Loonewalks above is valid for this case. 6 is the length of the shortest path from the starting point to the ending point. Hence, we need to find the number of shortest paths. Each such path has 4 moves to the right R and two moves up (U). All paths having 4 Rs and 2 Us are valid, as none of them will take the walker outside the grid. This is just the number of arrangements of 4 R and 2 U in any order, which can be seen to be 15. Hence the result is 15.

Example Input 2

3,3,6
1, 1, 3, 3
Output
90
Explanation
M=3,  N=3, k=6

The starting and ending points are (1,1) and (3,3) respectively.The shortest path is of length 4, and has two R and two U in the path. An example is RRUU. As the desired path length is 6, we need to add an additional R (and the corresponding L) to all the shortest paths, or add an additional U (and the corresponding D) to all the shortest paths.

Let us first consider adding one R and one L. The shortest path will have two R, and if we look at only the horizontal part of the path, the new sequence could be one of three, LRRR, RLRR or RRLR. Note that RRRL is not valid, as it will go outside the grid. We need to add two U to each of these.

In say RLRR, there are 5 ways if the two Us are together (UURLRR, RUULRR, and so on), and 10 ways if the Us are separate (URULRR, URLURR and so on), a total of 15 ways.

Hence for all the three sequences, there are 45 paths if a RL pair is added.Similar considerations show that if we add a UD pair, there are another 45 paths. The total number of paths with length exactly 6 is therefore 45 + 45=90, which is the result.


'''


def shortest_path(start_x, start_y, end_x, end_y):
    dist = abs(start_x - end_x) + abs(start_y - end_y)
    return dist

def find_paths(path, curr_x, curr_y, end_x, end_y,  k, boundary):
    if (path ==k and curr_x == end_x and curr_y == end_y):
        return 1
    if (path >= k):
        return 0
    if (curr_x < boundary[0] or curr_x > boundary[2]):
        return 0
    if (curr_y < boundary[1] or curr_y > boundary[3]):
        return 0 
    if (shortest_path(curr_x, curr_y, end_x, end_y) + path > k):
        return 0

    ans = find_paths(path+1, curr_x+1, curr_y, end_x, end_y, k, boundary) + find_paths(path+1, curr_x-1, curr_y, end_x, end_y, k, boundary) + find_paths(path+1, curr_x, curr_y+1, end_x, end_y, k, boundary) + find_paths(path+1, curr_x, curr_y-1, end_x, end_y, k, boundary)
    
    return ans
    

n,m,k = list(map(int, input().split(',')))
start_x,start_y,end_x,end_y = list(map(int, input().split(',')))

boundary = [0,0, m,n]

if start_x == end_x and start_y ==end_y:
    total_ways = 0
else:
    total_ways = find_paths(0, start_x, start_y, end_x, end_y, k , boundary)

print(total_ways)
