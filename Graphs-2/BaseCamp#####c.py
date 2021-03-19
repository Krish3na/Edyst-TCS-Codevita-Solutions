'''

Base Camp
Base Camp
Three friends set out to explore a remote area. They choose a safe place and make it their Base Camp. To speed up exploration time they decide to work independently. At any given point, either one or more of them can set out to explore the area. They set a protocol that after exploring the area they must meet back at the Base Camp in the evening and exchange notes.

The remote area consists of accessible and inaccessible pieces of land. Being ordinary humans, they must walk only the accessible piece of land. In order to maximize their exploration time, each one is interested in knowing about a shortest path back to the base camp.

Given that the area under exploration is arranged in form of a rectangular grid, help the explorers to chalk out a shortest path back to the base camp. Properties of a rectangle can be used as heuristic in computing distance between their positions and the Base Camp. Your task is to find out and mark the shortest path for each explorer and print each path as a separate grid.

The input and output specification sections describe how inputs will be provided on console and how output is expected back on console.

Input Format:
First line of input contains grid dimensions delimited by space character
Next rows number of lines contain column number of characters
Valid characters are {s, d, w, -}, where
s represents the location of the explorer
d represents the location of the base camp
w represents inaccessible region
- represents accessible region
End of input is marked by -1 character
Output Format:
Number of grids in the output should be same as number of explorers i.e. s characters in the input grid
Each output grid should be of the same dimension as the input grid
Each output grid should contain path from explorer location s to base camp location d
If there are more than one explorers, explorer with smallest value should be printed first in the output. Next smallest explorer location should be printed next followed by the last explorer grid.
First explorer path should be marked by a character, second by b character and third by c character
The s character in the grid must be replaced by {a, b or c} whichever is appropriate for the given explorer
The s character(s) in the grid must be replaced by - character for other explorer(s)
Output grids must be separated by a blank line
See example section for better understanding
Constraints:
It is guaranteed that there will always be exactly one shortest path for one explorer from a given location
Sample Input and Output
Input

4 4
w - d -
w - w -
w - w w
s - - s
-1
Output

w - d -
w a w -
w a w w
a - - -
 
w - d -
w b w -
w b w w
- - b b
Explanation

basecamp1

basecampe2

Input

4 4
s - - s
- - - -
- - - -
s - - d
-1
Output

a - - -
- a - -
- - a -
- - - d
 
- - - b
- - - b
- - - b
- - - d
 
- - - -
- - - -
- - - -
c c c d


'''

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

int dx[] = {0, -1, 0, 1, -1, -1, 1, 1};
int dy[] = {-1, 0, 1, 0, -1, 1, -1, 1};

int n, m;
char ar[1001][1001];
int dis[1001][1001];
int pos[1001][1001];

void go(int X, int Y ){
	queue<int> x, y;
	x.push(X);
	y.push(Y);
	dis[X][Y] = 0;
	pos[X][Y] = -1;
	while( !x.empty() ){
		int XX = x.front(); x.pop();
		int YY = y.front(); y.pop();
		for( int i = 0; i < 8; i++ ){
			int xx = XX + dx[i];
			int yy = YY + dy[i];
			if( xx < 0 || yy < 0 || xx >= n || yy >= m ){}
			else if( ar[xx][yy] != 'w'){
				if( dis[xx][yy] > dis[XX][YY]+1 ){
					dis[xx][yy] = dis[XX][YY] + 1;
					//watch4(dis[xx][yy], dis[XX][YY], XX, YY);
					x.push(xx);
					y.push(yy);
					pos[xx][yy] = i;
				}
			}
		}
	}
}

void print(int x, int y, int add){
	char a[n][m];
	for( int i = 0; i < n; i++ ){
		for( int j = 0; j < m; j++ ){
			a[i][j] = '-';
		}
	}
	
	while( ar[x][y] != 'd' ){
		
		a[x][y] = 'a' + add;
		int i = pos[x][y];
		x -= dx[i];
		y -= dy[i];
	}
	a[x][y] = 'd';
	for( int i = 0; i < n; i++ ){
		for( int j = 0; j < m; j++ ){
			if( ar[i][j] == 'w' )a[i][j] = 'w';
			cout << a[i][j] << " ";
		}
		cout << endl;
	}
}

int main(){
	int x, y;
	cin >> n >> m;
	for( int i = 0; i < n; i++ ){
		for( int j = 0; j < m; j++ ){
			cin >> ar[i][j];
			dis[i][j] = 100000;
			if( ar[i][j] == 'd' )x = i, y = j;
		}
	}
	go(x, y);
	
    int cnt = 0;
	
    for( int i = 0; i < n; i++ ){
		for( int j = 0; j < m; j++ ){
			if( ar[i][j] == 's' ){
				print(i, j, cnt++);
				cout << endl;
			}
		}
	}
}
