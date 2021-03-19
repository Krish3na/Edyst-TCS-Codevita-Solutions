'''
Minimum String Rotations
A rotation on a string is defined as removing first element and concatenating it at the end.

Given N, and an array of N strings, print the minimum no. of cumulative rotations on the strings so as to make all the strings equal.

If this is not possible return -1

Input format
The first line contains N, the number of strings
This is followed by N strings
Constraints
2 <= N <= 104
3 <= string length <= 100
All characters are in uppercase
Example Input
4
AABCD
CDAAB
DAABC
AABCD
Output
3
Explanation
Finally, all the string will become aabcd. First and last strings require no rotations.
Second string requires 2 rotations
Last string requires 1 rotation
Hence total rotations required are 3
'''

'''
1. Take input
2. Get all unique rotations
3. Increase vote of each unique rotation
4. for each rotation, also store if all strings contributed
'''


def rotate(word, k):
    new_word = word[k:] + word[:k]
    return new_word

n = int(input())
all_words = []
all_rotations = {}
min_rotations = 10**6
lengths = set()
for case in range(n):
    curr_word = input()
    curr_rotations = set()
    lengths.add(len(curr_word))

    if len(lengths) > 1:
        print(-1)
        exit(0)

    for i in range(0,len(curr_word)):
        rot_word = rotate(curr_word, i)
        #print(rot_word, case)
        if rot_word in curr_rotations:
            continue
        if rot_word in all_rotations:
            all_rotations[rot_word]+=i
        elif case == 0:
            all_rotations[rot_word]=i
            curr_rotations.add(rot_word)
        else:
            #print(rot_word, case, 'caused')
            print(-1)
            exit(0)
        
        if case == n-1:
            min_rotations = min(min_rotations,all_rotations[rot_word])
    
print(min_rotations)
