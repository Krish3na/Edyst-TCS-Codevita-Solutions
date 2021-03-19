'''

Accico Equi Pairs
Accico Equi Pairs
Ron Wesley has been bit by a three headed snake and Harry Potter is searching for a potion. The Witch promises to tell the ingredients of the medicine if Harry can find equi pair of an array. Listen to the conversation between Harry The witch to know more about equi pairs.

Conversation:-

The Witch: To find the equi pair, you must know how to find the slices first.
Harry: What is a slice?
The Witch: If Z is an array with N elements, a slice of indices (X, Y) is Z[X] + Z[X+1]…Z[Y]
Harry: How can I use it to find equi pair?
The Witch: (a, b) is an equi pair if slice of (0, a-1) = slice of (a+1, b-1) = slice of (b+1, N-1) and b>a+1 and size of array > 4

In the case that multiple equi pairs are possible, pick the one for which the middle slice contains the least number of elements.

Input Format:
An array of N integers delimited by white space

Output Format:
Print equi pair in first line in the format { a,b }
Print slices in the format { 0,a-1 }, { a+1,b-1 }, { b+1,N-1 }
OR

Print “Array does not contain any equi pair” if there are no equi pairs in the array
Constraints:
Zi >= 0 and 1 <= i <=N
size of array (N): 4 < N < 10^6
b > (a+1)
Sample Input and Output
Input

8 3 5 2 10 6 7 9 5 2

Output

Indices which form equi pair { 3,6 }
Slices are { 0,2 },{ 4,5 },{ 7,9 }
Explanation

Here index { 3,6 } is an equi pair.
Because Slice of { 0,2 } = 8+3+5=16 is equal to Slice of { 4,5 } = 10+6 = 16 and it is equal to Slice of { 7,9 } = 9+5+2 = 16

Input

6 2 6 2 3 3 1 9

Output

Array does not contain any equi pair

-----------------------------------------------------------------------------

Accico Equi Pair - Approach
This question, asked in CodeVita, is a good candidate to apply the 2 pointers approach.

Why? Well, a question is suitable for 2 pointers approach in arrays when we cannot afford to have a O(n^2) approach.

What does this mean? In the given question, it says that N, the size of the array, can go up to 10^6. This means that there could be a maximum of a million numbers in the array! If we use an approach that keeps checking for all possible combinations or keeps going back in the array, then it will take too much time.

For such arrays, we need to be able to give the answer in just 1 pass of the array.

Let’s see how we can solve the given question using the 2 pointers approach.

Understanding the question
Note that, essentially the question wants us to produce 3 slices of equal sum. That is to say that, we have to balance 3 things: the left sum, the middle sum, the right sum.

As we saw in the Pair with difference k problem, such a problem can be solved using 2 pointers.

We will begin by taking the slices to be as follows:

left part contains the sum of the left side of the array. We begin with left only containing first element
right part contains the sum of the right side of the array. We begin with the right only containing the last element
middle part contains the sum of the remaining elements
Depending on the scenarios, these are the decisions we should make:

Scenario	Decision	Explanation
left == right == middle	We have found our slice! Try finding a smaller middle slice, if possible. Else, return	As per the question’s guidelines
left > middle	return false	left can only increase by including more numbers in the left slice. If it’s already greater than middle, then nothing can be done
right > middle	return false	right can only increase by including more numbers in the right slice. If it’s already greater than middle, then nothing can be done
left < right	increase left slice, decrease middle slice	balancing the slices
right < left	increase right slice, decrease middle slice	balancing the slices
So far, we’ve covered most of the test cases. Yet, there is 1 more remaining:

(left == right) && (right != middle) && (left != middle)
In this case, we should either choose to increase left only if left can become equal to middle
Otherwise, we should increase right only if right can become equal to middle
If both aren’t possible, increase left and right and then repeat the loop again from the start (refer to the table)
And before we wrap this up, there is one more thing we need to consider:
Zi >= 0

This means that the array might consider zeros. What does this imply? Simply increasing left or right will not help us - we should keep increasing them till we encounter a non-zero number. Otherwise left or right sum will never increase.

Pseudo-code
a = 1, b = a.length-2 // initial slice
left_sum = Z[0], right_sum = Z[Z.length-1]
 
// ignoring all zeros
while b > a + 1
    while Z[a] == Z[a + 1] == 0:
        a += 1
    while Z[b] == Z[b - 1] == 0:
        b -= 1
 
    middle = sumZ - left_sum - right_sum - Z[a] - Z[b]
    if (left > middle) or (right > middle):
        return False
 
    if left == middle == right:
        printAnswer(a, b) // use this function to print in correct format
        return True
 
    if left < right:
        left += Z[a]
        a += 1
    
    else if left > right:
            right += Z[b]
            b -= 1
        else:
            if left + Z[a] == middle - Z[a + 1]:
                left += Z[a]
                a += 1
            elif right + Z[b] == middle - Z[b - 1]:
                right += Z[b]
                b -= 1
            else:
                left += Z[a]
                a += 1
                right += Z[b]
                b -= 1
 
    print("Array does not contain any equi pair")
    return False
'''


def printAnswer(a, b):
    print(f"Indices which form equi pair {{ {a},{b} }}")
    print(f"Slices are {{ 0,{a-1} }},{{ {a+1},{b-1} }},{{ {b+1},{len(Z)-1} }}")


def solve(Z):
    assert len(Z) > 4

    sumZ = sum(Z)

    # print(Z)

    a, b = 1, len(Z) - 2
    left, right = Z[0], Z[-1]

    while b > a + 1:
        while Z[a] == Z[a + 1] == 0:
            a += 1
        while Z[b] == Z[b - 1] == 0:
            b -= 1

        middle = sumZ - left - right - Z[a] - Z[b]

        # print(a, b, left, middle, right)

        if (left > middle) or (right > middle):
            print("Array does not contain any equi pair")
            return False

        if left == middle == right:
            printAnswer(a, b)
            return True

        if left < right:
            left += Z[a]
            a += 1
        elif left > right:
            right += Z[b]
            b -= 1
        else:
            # at this point, no matter which move we make (inc a or dec b)
            #   middle will change (thanks to the while loops above)
            if left + Z[a] == middle - Z[a + 1]:
                left += Z[a]
                a += 1
            elif right + Z[b] == middle - Z[b - 1]:
                right += Z[b]
                b -= 1
            else:
                left += Z[a]
                a += 1
                right += Z[b]
                b -= 1

    print("Array does not contain any equi pair")
    return False


if __name__ == "__main__":
    Z = list(map(int, input().strip().split()))
    solve(Z)

