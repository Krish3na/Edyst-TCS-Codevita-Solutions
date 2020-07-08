'''
Cyclic Palindrome
Cyclic Palindrome
A string is said to be palindrome, if it reads the same from both the ends. Given a string S, you are allowed to perform cyclic shifts. More formally, you can pick any one character from any end (head or tail) and you can append that character at the other end. For example, if the string is abc, then if we do a shift using the character at head position then the string becomes bca. Similarly, if we do the shift using the character at the tail then the input string becomes cab. Your task is to find out the minimum number of shifts needed to make the given string, a palindrome.

In case, we can’t convert the string to palindrome then print -1.

Input Format
First line starts with T i.e. number of test cases, and then T lines will follow each containing a string S.

Output Format
Print the minimum number of cyclic shifts for each string if it can be made a palindrome, else -1.

Constraints
1<=T<=100
1<=|S|<=300, S will contains only lower case alphabets a-z.

Sample Input and Output
Input

4
abbb
aaabb
aabb
abc
Output

-1
1
1
-1
Explanation:

For Test Case 2 (aaabb):

Shift the character at the tail to the head and the result will be baaab, which is a palindrome. This is an operation which requires minimum number of shifts to make the given string a palindrome.

For Test Case 3 (aabb):

One way to convert the given string to palindrome is, shift the character at the head to the tail, and the result will be abba, which is a palindrome. Another way is to shift the character at the tail to the head, and the result will be baab, which is also a palindrome. Both require only one shift.
'''

def leftshift(s):
    n=len(s)
    nw_s=s[n-1]+s[:n-1]
    return nw_s

def rightshift(s):
    n=len(s)
    nw_s=s[1:]+s[0]
    return nw_s

def ispalin(s):
    n=len(s)
    for i in range(n//2):
        if s[i]!=s[n-i-1]:
            return False
    return True

t=int(input())
for i in range(t):
    s=input()
    left_s=right_s=s
    shifts=0
    while shifts<=len(s)//2:
        if ispalin(left_s) or ispalin(right_s):
            print (shifts)
            break
        left_s=leftshift(left_s)
        right_s=rightshift(right_s)
        shifts+=1
    else:
        print(-1)
        
