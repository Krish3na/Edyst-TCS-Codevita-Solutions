'''
Longest Possible Route
Longest Possible Route
Given an MxN matrix, with a few hurdles arbitrarily placed, calculate the cost of longest possible route from point A to point B within the matrix.

Input Format:
First line contains 2 numbers delimited by whitespace where, first number M is number of rows and second number N is number of columns
Second line contains number of hurdles H followed by H lines, each line will contain one hurdle point in the matrix.
Next line will contain point A, starting point in the matrix.
Next line will contain point B, stop point in the matrix.
Output Format:
Output should display the length of the longest route from point A to point B in the matrix.

Constraints:
The cost from one position to another will be 1 unit.
A location once visited in a particular path cannot be visited again.
A route will only consider adjacent hops. The route cannot consist of diagonal hops.
The position with a hurdle cannot be visited.
The values MxN signifies that the matrix consists of rows ranging from 0 to M-1 and columns ranging from 0 to N-1.
If the destination is not reachable or source/ destination overlap with hurdles, print cost as -1.
Sample Input and Output
Input

3 10
3
1 2
1 5
1 8
0 0
1 7 
Output

24
Explanation

Here matrix will be of size 3x10 matrix with a hurdle at (1,2),(1,5) and (1,8) with starting point A(0,0) and stop point B(1,7)

3 10
3 -- (no. of hurdles )
1 2
1 5
1 8
0 0 -- (position of A)
1 7 -- (position of B)
So if you examine matrix below shown in Fig 1, total hops

longest_possible_route

=> count is 24. So final answer will be 24. No other route longer than this one is possible in this matrix.

Input

2 2
1
0 0
1 1
0 0 
Output

-1
Explanation

No path is possible in this 2*2 matrix so answer is -1

'''

#define __gcd(a, b) __algo_gcd(a, b)
#include<set>
#include<map>
#include<cmath>
#include<stack>
#include<queue>
#include<array>
#include<cstdio>
#include<bitset>
#include<vector>
#include<utility>
#include<sstream>
#include<cstring>
#include <climits>
#include <fstream>
#include<iostream>
#include<iomanip>
#include<algorithm>
#include <functional>
using namespace std;

int M, N;
int mat[1001][1001];
int visited[1001][1001];

bool isSafe(int x, int y)
{
	if (mat[x][y] == 0 || visited[x][y])
		return false;

	return true;
}

bool isValid(int x, int y)
{
	if (x < M && y < N && x >= 0 && y >= 0)
		return true;
	
	return false;
}

void findLongestPath(int i, int j, int x, int y, int& max_dist, int dist)
{
	if (i == x && j == y) 
	{
		max_dist = max(dist, max_dist);
		return;
	}
	
	visited[i][j] = 1;
	
	if (isValid(i + 1, j) && isSafe(i + 1, j))
		findLongestPath(i + 1, j, x, y, max_dist, dist + 1);
	
	if (isValid(i, j + 1) && isSafe(i, j + 1))
		findLongestPath(i, j + 1, x, y, max_dist, dist + 1);
	
	if (isValid(i - 1, j) && isSafe(i - 1, j))
		findLongestPath(i - 1, j, x, y, max_dist, dist + 1);
	
	if (isValid(i, j - 1) && isSafe(i, j - 1))
		findLongestPath(i, j - 1, x, y, max_dist, dist + 1);
	
	visited[i][j] = 0;
}

int main()
{
	cin >> M >> N;
	for( int i = 0; i < M; i++ ){
		for( int j = 0; j < N; j++ ){
			mat[i][j] = 1;
		}
	}
	int q;
	cin >> q;
	while( q-- ){
		int u, v;
		cin >> u >> v;
		mat[u][v] = 0;
	}
	memset(visited, 0, sizeof visited);
	int max_dist = -1;
	int x, y, X, Y;
	cin >> x >> y >> X >> Y;
	findLongestPath(x, y, X, Y, max_dist, 0);
	cout << max_dist;
	return 0;
}
