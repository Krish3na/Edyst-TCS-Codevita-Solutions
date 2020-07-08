
'''
Exchange Digits
Compute nearest larger number by interchanging digits updated.

Given 2 numbers a and b find the smallest number greater than b by interchanging the digits of a and if not possible print -1

Constraints
1 <= a,b <= 10000000

Input Format
2 numbers, a and b, separated by space.

Output
A single number, greater than b

If not possible, print -1.

Test Case
Input

459 500

Output

549

Input

645757 457765

Output

465577

Input

5964 9984

Output

-1

'''

from itertools import permutations
i1,i2=map(int,input().split())
a=list(str(i1))
b=list(str(i2))
re=[]
for p in set(permutations(a,len(a))):
    k=(''.join(list(p)))
    if (k[0]!='0' and int(k)>i2):
        re.append(k)

try:
    print(min(re))
except:
    print(-1)
    
