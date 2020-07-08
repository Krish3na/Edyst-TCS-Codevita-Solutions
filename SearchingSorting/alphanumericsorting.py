'''
Alpha Numeric Sorting
Given text comprising of words and numbers, sort them both in ascending order and print them in a manner that a word is followed by a number. Words can be in upper or lower case. You have to convert them into lowercase and then sort and print them.

Input Format
First line contains total number of test cases, denoted by N
Next N lines, each contains a text in which words are at odd position and numbers are at even position and are delimited by space
Output Format:
Words and numbers sorted in ascending order and printed in a manner that a word is followed by a number.

Constraints:
Text starts with a word
Count of words and numbers are the same.
Duplicate elements are not allowed
Words should be printed in lower case.
No special characters allowed in text.
Sample Input & Output
Input

2
Sagar 35 sanjay 12 ganesH 53 ramesh 19
Ganesh 59 suresh 19 rakesh 26 laliT 96
Output

ganesh 12 ramesh 19 sagar 35 sanjay 53
ganesh 19 lalit 26 rakesh 59 suresh 96

'''

t=int(input())
for i in range(t):
    text=input().split()
    words=[]
    numbers=[]
    for i in range(0,len(text)//2):
        words.append(text[2*i].lower())
    for i in range(0,len(text)//2):
        numbers.append(int(text[(2*i)+1]))
    words.sort()
    numbers.sort()
    for i in range(len(words)):
        print(words[i],numbers[i],end=' ')
    print()
        
