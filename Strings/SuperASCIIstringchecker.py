'''

Super ASCII String Checker
Super ASCII String Checker
In the Byteland country a string S is said to super ascii string if and only if count of each character in the string is equal to its ascii value.

In the Byteland country ascii code of a is 1, b is 2 …z is 26.

Your task is to find out whether the given string is a super ascii string or not.

Input Format:
First line contains number of test cases T, followed by T lines, each containing a string S.

Output Format:
For each test case print Yes if the String S is super ascii, else print No

Constraints
1<=T<=100
1<=|S|<=400, S will contains only lower case alphabets ('a'-'z')
Sample Input and Output
Input

2
bba
scca

Output

Yes
No

In case 1, viz. String "bba" -
The count of character 'b' is 2. Ascii value of 'b' is also 2.
The count of character 'a' is 1. Ascii value of 'a' is also 1.
Hence string "bba" is super ascii.

'''

t=int(input())
for i in range(t):
    string=input().strip()
    arr=[0]*26
    for i in string:
        arr[ord(i)-97]+=1   
    flag=0
    for i in range(len(arr)):
        if arr[i]==i+1 or arr[i]==0:
            flag=1
        else:
            flag=0
            break
    if flag==1:
        print('Yes')
    else:
        print('No')
