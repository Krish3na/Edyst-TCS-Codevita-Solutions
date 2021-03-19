'''

N Queens Problem
This is the famous N Queens problem. In a chessboard of size NxN, you must place N queens on the chessboard such that none of the Queens attack each other.

For example if we have the following configuration:

* * * Q *
Q * * * *
* Q * * *
* * Q * *
* * * * Q
Q = Queen & * = blank.

Such a formation will result in the killing of the Queens in the first 3 columns. It is up to you to figure out how to place these Queens.

Given an N x N chessboard, you have to place N queens such that they don't kill each other.

Write a method Met that takes as parameter a 2D character array with only * and returns a 2D array that has Q in the appropriate positions.

Note: Array is larger than 3x3. If there is more than 1 solution, then return any of the solutions.

We are going to check your output against a custom solution checker. To check your own output, please check your own local compilers.

Example Input:

* * * *
* * * *
* * * *
* * * *
Output:

* Q * * 
* * * Q
Q * * *
* * Q *

'''

""" Python3 program to solve N Queen Problem using 
backtracking """


""" A utility function to print solution """
def printSolution(board): 
	for i in range(N): 
		for j in range(N): 
			print(board[i][j], end = " ") 
		print() 

""" A recursive utility function to solve N 
Queen problem """
def solveNQUtil(board, col): 
	
	""" base case: If all queens are placed 
		then return True """
	if (col >= N): 
		return True
		
	""" Consider this column and try placing 
		this queen in all rows one by one """
	for i in range(N): 
		
		""" Check if the queen can be placed on board[i][col] """
		""" A check if a queen can be placed on board[row][col]. 
		We just need to check ld[row-col+n-1] and rd[row+coln] 
		where ld and rd are for left and right diagonal respectively"""
		if ((ld[i - col + N - 1] != 'Q' and
			rd[i + col] != 'Q') and cl[i] != 'Q'): 
				
			""" Place this queen in board[i][col] """
			board[i][col] = 'Q'
			ld[i - col + N - 1] = rd[i + col] = cl[i] = 'Q'
			
			""" recur to place rest of the queens """
			if (solveNQUtil(board, col + 1)): 
				return True
				
			""" If placing queen in board[i][col] 
			doesn't lead to a solution, 
			then remove queen from board[i][col] """
			board[i][col] = '*' # BACKTRACK 
			ld[i - col + N - 1] = rd[i + col] = cl[i] = '*'
			
			""" If the queen cannot be placed in 
			any row in this colum col then return False """
	return False
	
""" This function solves the N Queen problem using 
Backtracking. It mainly uses solveNQUtil() to 
solve the problem. It returns False if queens 
cannot be placed, otherwise, return True and 
prints placement of queens in the form of 1s. 
Please note that there may be more than one 
solutions, this function prints one of the 
feasible solutions."""
def solveNQ(board): 
	if (solveNQUtil(board, 0) == False): 
		printf("Solution does not exist") 
		return False
	printSolution(board) 
	return True
	
# Driver Code
board=[]
n=list(input().split())
board.append(n)
for i in range(len(n)-1):
    l=list(input().split())
    board.append(l)

N =len(n)

""" ld is an array where its indices indicate row-col+N-1 
(N-1) is for shifting the difference to store negative 
indices """
ld = [0] * 30

""" rd is an array where its indices indicate row+col 
and used to check whether a queen can be placed on 
right diagonal or not"""
rd = [0] * 30

"""column array where its indices indicates column and 
used to check whether a queen can be placed in that 
	row or not"""
cl = [0] * 30
    
solveNQ(board) 

