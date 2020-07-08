'''
CodeVita 2013, Jumble With Numbers
Jumble With Numbers
In NASA, two researchers, Mathew and John, started their work on a new planet, but while practicing research they faced a mathematical difficulty. In order to save the time they divided their work.

So scientist Mathew worked on a piece and invented a number computed with the following formula:
A Mathew number is computed as follows using the formula:
H(n) = n(2n-1)

And scientist John invented another number which is built by the following formula which is called John number.
T(n) = n(n+1)/2

Now Mathew and John are jumbled while combining their work. Now help them combine their research work by finding out number in a given range that satisfies both properties.

Using the above formula, the first few Mathew-John numbers are:
1 6 15 28...

Input Format
Input consists of 3 integers T1,T2,M separated by space. T1 and T2 are upper and lower limits of the range. The range is inclusive of both T1 and T2. Find Mth number in range [T1,T2] which is actually a Mathew-John number.

Constraints
0 < T1 < T2 < 1000000
Output Format
Print Mth number from formed sequence between T1 and T2 (inclusive).

For Valid Input,print

Print Mth number from formed sequence between T1 and T2

Or

No number is present at this index

For Invalid Input,print

Invalid Input

Sample Input / Output
Input

90 150 2
Output

120
Input

20 80 6
Output

No number is present at this index
Input

-5 3 a
Output

Invalid Input
'''
t1,t2,m=input().split()
if m.isnumeric()==0 or t1.isnumeric()==0 or t2.isnumeric()==0 :
    print('Invalid Input')
else:
    l=[]
    for i in range(1,1000):
        cal=i*(2*i-1)
        if cal>=int(t1) and cal<=int(t2):
            l.append(cal)
            if cal >int(t2):
                break

    if int(m)<=len(l):
        print(l[int(m)-1])
    else:
        print('No number is present at this index')





