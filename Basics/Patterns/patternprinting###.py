'''
Pattern Printing
Decode the logic and print the Pattern that corresponds to given input.

If N= 3

then pattern will be :

10203010011012
**4050809
****607
If N= 4, then pattern will be:

1020304017018019020
**50607014015016
****809012013
******10011
Constraints
2 <= N <= 100
Input Format
First line contains T, the number of test cases
Each test case contains a single integer N
Output
First line print Case #i where i is the test case number
In the subsequent line, print the pattern
Test Case 1
3
3
4
5
Output
Case #1
10203010011012
**4050809
****607
Case #2
1020304017018019020
**50607014015016
****809012013
******10011
Case #3
102030405026027028029030
**6070809022023024025
****10011012019020021
******13014017018
********15016

'''
t=int(input())
for _ in range(1,t+1):
    n=int(input())
    print('Case #%d'%_)
    tot=n*n+1
    val=1
    val1=n*n+1
    val2=val1
    for i in range(1,n+1):
        for j in range(1,i):
            print("**",end='')
        for k in range(1,n-i+2):
            print(val,end='0')
            val+=1
        for l in range(n+1,n+n+2-i):
            if l==n+n+1-i:
                print(val1,end='')
            else:
                print(val1,end='0')
            val1+=1
        print()
        val2=val2-(n-i)
        val1=val2

