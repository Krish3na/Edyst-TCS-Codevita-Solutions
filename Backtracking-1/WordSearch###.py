'''

Word Search
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input Format
First line contains N number of rows and M number of columns
2D board with NxM dimension follows
Last line of input contains a word S
Output Format
Print true or false based on whether the word appears in the grid or not

Constraints
board and word consists only of lowercase and uppercase English letters.
1 <= N <= 200
1 <= M <= 200
1 <= |S| <= 10^3
Sample Input
3 4
A B C E
S F C S
A D E E
ABCCED
Sample Output
true
Explanation
A B C E

S F C S

A D E E

'''

def solve(i,j, index,word, grid):
###Base Case
	if i < 0 or i >= len(grid) or j <0 or j>= len(grid[i]):
		#print(grid[i][j], word[index], False)
		return False
	if index >= len(word):
		return True
	if grid[i][j] != word[index]:
		#print(grid[i][j], word[index], False)
		return False
###Recursive Case
	temp = grid[i][j]
	ans = False
	if word[index] == grid[i][j]:
		grid[i][j] = '$'
		ans = solve(i,j+1,index+1, word, grid) or solve(i+1, j, index+1, word, grid) or solve(i-1, j, index+1, word, grid) or solve(i, j-1, index+1, word, grid)
		grid [i][j] = word[index]
	
	return ans

row, col = list(map(int, input().split()))
grid = []

for i in range(row):
    grid.append(input().split())

word = input()
        
#print(grid)
#print(word)
ans = False
for i in range(row):
    for j in range(col):
        if solve(i,j,0, word, grid):
            ans = True
            break
    if(ans):
        break
if(ans):
    print("true")
else:
    print('false')
