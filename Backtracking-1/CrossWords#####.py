'''

Cross Words
Cross Words
A crossword puzzle is a square grid with black and blank squares, containing clue numbers (according to a set of rules) on some of the squares. The puzzle is solved by obtaining the solutions to a set of clues corresponding to the clue numbers.

The solved puzzle has one letter in each of the blank square, which represent a sequence of letters (consisting of one or more words in English or occasionally other languages) running along the rows (called Across, or A) or along the columns (called Down or D). Each numbered square is the beginning of an Across solution or a Down solution. Some of the across and down solutions will intersect at a blank square, and if the solutions are consistent, both of them will have the same letter at the intersecting square.

In this problem, you will be given the specifications of the grid, and the solutions in some random order. The problem is to number the grid appropriately, and associate the answers consistently with the clue numbers on the grid, both as Across solutions and as Down solutions, so that the intersecting blank squares have the same letter in both solutions.

Rules for Clue Numbering

The clue numbers are given sequentially going row wise (Row 1 first, and then row2 and so on)

Only blank squares are given a clue number

A blank square is given a clue number if either of the following conditions exist (only one number is given even if both the conditions are satisfied)

It has a blank square to its right, and it has no blank square to its left (it has a black square to its left, or it is in the first column). This is the beginning of an Across solution with that number

It has a blank square below it, and no blank square above it (it has a black square above it or it is in the first row). This is the beginning of a Down solution with that number.

Constraints
5<=N<=15
5<=M<=50
Input Format
The input consists of two parts, the grid part and the solution part

The first line of the grid part consists of a number, N, the size of the grid (the overall grid is N x N) squares. The next N lines correspond to the N rows of the grid. Each line is comma separated, and has number of pairs of numbers, the first giving the position (column) of the beginning of a black square block, and the next giving the length of the block. If there are no black squares in a row, the pair 0,0 will be specified. For example, if a line contains 2,3,7,1,14,2, columns 2,3,4 (a block of 3 starting with 2), 7 (a block of 1 starting with 7) and 14,15 (a block of 2 starting with 14) are black in the corresponding row.

The solution part of the input appears after the grid part. The first line of the solution part contains M, the number of solutions. The M subsequent lines consist of a sequence of letters corresponding to a solution for one of the Across and Down clues. All solutions will be in upper case (Capital letters)

Output
The output is a set of M comma separated lines. Each line corresponds to a solution, and consists of three parts, the clue number, the letter A or D (corresponding to Across or Down) and the solution in to that clue (in upper case)

The output must be in increasing clue number order. If a clue number has both an Across and a Down solution, they must come in separate lines, with the Across solution coming before the Down solution.

Sample Input & Output
Input

5
5,1
1,1,3,1,5,1
0,0
1,1,3,1,5,1
1,1
5
EVEN
ACNE
CALVE
PLEAS
EVADE
Output

1,A,ACNE
2,D,CALVE
3,D,EVADE
4,A,PLEAS
5,A,EVEN
Explanation

N is 5, and the disposition of the black squares are given in the next 5 (N) lines. The grid looks like this

crossword1

M=5, and there are 5 (M) solutions.
If the grid is numbered according to the rules, the numbered grid loos like this. Note that row 3 has no blanks, and the input line says 0,0

crossword2

The solutions are fitted to the grid so that they are consistent, and the result is shown below. Note that this is consistent, because the letter at each intersecting blank square in the Across solution and the Down solution.

crossword3

Based on this the output is given in clue number order. 1 Across is ACNE, and hence the first line of the output is 1,A,ACNE. The same logic gives all the remaining solutions.


Input

5
1,1
1,1,3,2
0,0
1,1,3,2
0,0
5
ASIAN
RISEN
FEAR
CLAWS
FALLS
Output

1,A,FEAR
1,D,FALLS
2,D,RISEN
3,A,CLAWS
4,A,ASIAN
Explanation

N=5, and the grid looks like this

crossword4

M=5, and the 5 solutions are given

The numbered grid looks like this

crossword5

The consistently populated grid (with the solutions) look like this

crossword6

The output can be easily given from this. Note that clue number 1 has both an Across solution (FEAR) and a DOWN solution (FALLS). The Across solution must precede the Down solution in the output.


'''





# set the default BLOCK and BLANK characters
BLOCK = " "
BLANK = "."

# for a given index (i, j) fetch k characters based on the direction ('A' or 'D')
# returns a list
def getWord(grid, direction, i, j, k):
    if direction == "A":
        return grid[i][j : j + k]
    if direction == "D":
        return [grid[x][j] for x in range(i, i + k)]


# give the current position of characters, tells if the word can be placed
# (overlaps)
def canPlaceWord(current, candidate):
    if len(candidate) != len(current):
        return False

    for x in range(len(candidate)):
        if current[x] != BLANK and current[x] != candidate[x]:
            return False

    return True


# places word on the grid at the given clue position and direction
def addWord(grid, direction, i, j, k, word):
    if direction == "A":
        for x in range(k):
            grid[i][j + x] = word[x]
        return grid
    if direction == "D":
        for x in range(k):
            grid[i + x][j] = word[x]
        return grid


# prints the grid
def printGrid(grid):
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            print(grid[i][j], end="")
        print()
    print()


# finds and numbers the clues based on the grid
# returns an array of clues, each of which is a list [n, d, i, j, k, w] where,
#   n, d is the clue number and direction
#   i, j is the starting index of the clue on the grid
#   k is the length of the clue
#   w is the current solution (set to None initially) to the clue
def numberGrid(grid):
    clues = []
    n = 1
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            if grid[i][j] == BLANK:
                hasBlankToRight = j + 1 < len(grid) and grid[i][j + 1] == BLANK
                hasBlockToLeft = j == 1 or grid[i][j - 1] == BLOCK
                hasBlankToDown = i + 1 < len(grid) and grid[i + 1][j] == BLANK
                hasBlockToUp = i == 1 or grid[i - 1][j] == BLOCK

                isAcross = hasBlankToRight and hasBlockToLeft
                isDown = hasBlankToDown and hasBlockToUp

                if isAcross:
                    k = 0
                    while j + k < len(grid[0]) and grid[i][j + k] == BLANK:
                        k += 1
                    clues.append([n, "A", i, j, k, None])

                if isDown:
                    k = 0
                    while i + k < len(grid) and grid[i + k][j] == BLANK:
                        k += 1
                    clues.append([n, "D", i, j, k, None])

                if isAcross or isDown:
                    n += 1

    return clues


# given the clue number, and direction; sets the solution to that clue in the
#   clues list
def setClueSolution(clues, n, d, word):
    for clue in clues:
        if clue[0] == n and clue[1] == d:
            clue[5] = word
            return


# given the clue number, and direction; sets the solution to that clue in the
#   clues list
def unsetClueSolution(clues, n, d):
    for clue in clues:
        if clue[0] == n and clue[1] == d:
            clue[5] = None
            return


"""
Solution Approach:

- Pick one word at a time from the list of words given in the question
- For that word, find all the possible clues it could be an answer to
- For each clue, guess that the current word is the answer
    - Fetch the current characters in the grid at the clue position
    - If the word chosen overlaps with the current characters, it means it can
        be placed on the grid.
    - Set the word as the answer to the clue
    - Recursively call solve on the next word
    - If that call returns False, it means that by placing the chosen word as
        the answer to the current clue, other words cannot be placed correctly.
        Thus, we have made a mistake and this is not the correct clue for the
        chosen word.
    - Choose the next clue, and repeat this process.
    - When we end up placing the word in its current position, the recursive
        call to solve(...) will have generated `True` (since it would have found
        a way to place all the remaining words in their correct positions; since
        our chosen word is in its correct position)
"""


def solve(grid, clues, words, idx):
    if idx == len(words):
        return True

    # the word this recursion of solve(...) is going to place in its correct position
    word = words[idx]

    # set of clues that this word can be the answer to
    validClues = {
        (n, d, i, j, k, w)
        for (n, d, i, j, k, w) in clues
        if len(word) == k and w is None
    }

    for (n, d, i, j, k, _) in validClues:
        current = getWord(grid, d, i, j, k)

        if canPlaceWord(current, word):
            addWord(grid, d, i, j, k, word)
            setClueSolution(clues, n, d, word)

            if solve(grid, clues, words, idx + 1):
                return True

            addWord(grid, d, i, j, k, current)
            unsetClueSolution(clues, n, d)

    return False


if __name__ == "__main__":
    N = int(input())
    # the grid is (N+1) x (N+1) with the 0th row, 0th column set as blanks
    #   we ignore the 0th row and column and focus on the remaining NxN grid
    #   so that our grid numbering stays consistent with the question
    grid = [[BLANK for i in range(N + 1)] for j in range(N + 1)]
    for i in range(1, N + 1):
        blocks = list(map(int, input().strip().split(",")))
        for j in range(0, len(blocks), 2):
            for k in range(blocks[j], blocks[j] + blocks[j + 1]):
                grid[i][k] = BLOCK

    clues = numberGrid(grid)

    M = int(input())
    words = [input().strip().upper() for _ in range(M)]

    solve(grid, clues, words, 0)

    for (n, d, i, j, k, w) in clues:
        print(f"{n},{d},{w}")
