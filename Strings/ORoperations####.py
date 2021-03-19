'''

OR Operations
Given an Array of N numbers, find the minimum number of elements (taken in any order) required to reach the maximum bitwise OR.

Constraints:

1 <= N <= 105
1 <= Ai <= 106
Input format

The first line contains T, the number of test cases. Each of the following T lines contain:
N followed by N numbers A1, A2, A3...... An
Output format

Print min elements required for each test case
Example Input

3
4 3 5 7 13
4 2 4 8 16
4 5 3 1 7
Output

2
4
1
Explanation:

Case 1: we have numbers: 3: 011, 5: 101, 7: 111, 13: 1101. Combining 13 and 7 will give us 15 : 1111, which is the maximum OR possible in this array. Thus answer is 2 - only 2 elements needed

Case 2: we need all 4 numbers to reach combined bitwise OR of  11110

Case 3: we only need 7 ( 111) to reach the maximum OR possible

'''
####################################################################################

'''
Before we solve this problem, let us observe what happens when any 2 numbers have an OR:

011 | 100 = 111

011 set bits are at positions: {0,1}

and for 100, the set bits are at position {2}

For final answer, set bit positions are {0,1,2}

We notice that, if we treat the numbers as which bits are set, then the OR of 2 numbers will give us the union of the set of the set bits.

That is, a | b | c will have the set bits that are setbits(a) U setbits(b) U setbits(c).

In the question, we have to find out the minimum number of sets which when we take the union, give us the same number of set as when the whole array is taken union.

This is atypical Set Cover Problem -  we encourage you to read about it.

This is what we shall do:

Take the OR of the entire array -  this is our target
Convert each integer into a set which contains the positions of the set bits
Then, first take that number which is closest to the target in terms of set bits.
Update the required target. And now search for another number which is is closest to our target
Repeat steps 3 & 4 till we reach our target
Print out the number of sets we have taken as the minimum count required
Luckily, the methods for set union are available in Python. In other languages you will need to define those methods

'''
# method to cerate a set of the set bits
def getSet(num):
    setBits = set()
    mask = 1
    for pos in range(0, 32):
        if (((mask << pos) & num ) > 0):
            setBits.add(pos)
    #print(setBits)
    return setBits

T = int(input())

for  _ in range(T):
    arr = list(map(int, input().split()))
    assert (len(arr[1:]) == arr[0])
    arr = arr[1:]
    count = 1

    maxOR = 0
    all_sets = []

	# get OR of entire array
    # also create sets for each number
    for num in arr:
        maxOR = num |  maxOR
        all_sets.append(getSet(num))
    #print(all_sets)

    # this is our target
    maxSet = getSet(maxOR)


    
    minSubset = [] # stores our final answer
    covered = set([]) # how many bits set so far
    while len(covered) != len(maxSet):
    	# get the set with max difference
        maxDifferenceSet = max(all_sets, key = lambda x: len(x - covered))
        covered = covered | maxDifferenceSet # union of 2 sets
        minSubset.append(maxDifferenceSet)

    print(len(minSubset))

