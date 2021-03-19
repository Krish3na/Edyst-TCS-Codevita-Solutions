'''
CodeVita 2015, Credit and Risk Calculator
Credit and Risk Calculator
Money Bank is an investment bank. It gives money to the companies for their operation that approach it. The bank’s officers have to calculate the maximum amount that the company can be given, based on the company’s market value and its market rating published by Global Rating Companies. The maximum amount will change on a daily basis as per the change in the company’s shares, its market value and its change in rating. Based on the maximum amount allocated, the bank internally calculates the amount that the company can use on a particular day. The maximum amount that the bank will give at any point is 50% of the company’s value, which will decrease as per the change in the company’s rating.

Example:
Company ABC has 25734 shares in the market. The current value of the share is 77 INR. The change in the Share Value from yesterday is +10 (or 10) Today’s rating of ABC is 87 (out of 100). The change in rating from yesterday is +2 (or 2). The credit and risk calculator will work in the following way -

No. Of Shares (N)	Share Value (SV)	Change in Share Value (CSV)	Previous Share Value (SV’) = SV-CSV	PCompany Value (CV) = N*min (SV, SV’)	Company Rating ®	Change in Rating ( CR)	Previous Rating (R’)= R-CR	PMax Credit Company is Eligible for (CE) =CV * (50%)	PCredit Allotted (CA) = CE * (min(R’, R)/100)
25734	77	10	67.00	= (N*67)
= 25734 * 67
= 1724178.00	87	2	85.00	= 1724178.00 *0.5
=862089.00	=(CE*85/100)
=862089 * 0.85
= 732775.65
Similarly, company XYZ has 30000 shares in the market. The current value of the share is 90 INR. The change in the Share Value from yesterday is -15. Today’s rating of XYZ is 83 (out of 100). The change in rating from yesterday is -4. The credit and risk calculator will work in the following way-

No. Of Shares (N)	Share Value (SV)	Change in Share Value (CSV)	Previous Share Value (SV’) = SV-CSV	PCompany Value (CV) = N*min (SV, SV’)	Company Rating ®	Change in Rating ( CR)	Previous Rating (R’)= R-CR	PMax Credit Company is Eligible for (CE) =CV * (50%)	PCredit Allotted (CA) = CE * (min(R’, R)/100)
30000	90	-15	105.00	2700000.0	83	-4	87	1350000.00	1120500.00
Input Format:
First line contains total number of test cases T
Each test case comprises of

First line contains number of shares N
Second line contains current share value SV
Third line contains change in share value CSV
Fourth line contains current rating R
Fifth line contains change in rating CR
Output Format:
In case of Valid inputs, print the following per line

Previous Share Value SV'
Previous Rating R'
Company Value CV
Maximum Credit CE
Credit Allotted CA

OR

Print Invalid Input in case of invalid input(s)

Constraints
**Highest Priority Constraint **
Share Value (SV and SV’) can never be negative

Input related constraints:-
1 <= T <=100
20000 <= N <= 10000000
20.00 <= SV <= 10000.00 (Note:- This is a numerical constraint only)
-2000.00 <= CSV <= 2000.00 (Note:- This is a numerical constraint only)
0.01 <= R <= 99.99 (Note:- This is a numerical constraint only)
-10.00 <= CR <= 10.00 (Note:- This is a numerical constraint only)

Calculation should be done upto 11-digit precision

The Change in Share Value (CSV) and Change in Rating (CR) are dependent as below:

If CSV is Positive, CR can be Positive or Negative.
If CSV is Negative, CR cannot be Positive.
Output related constraints:-

The values of CV, CE and CA are to be rounded to 2 Decimal Places, always to the Ceiling or Upper Value
The range of the calculated values are-

20.00 <= SV' <= 10000.00
0.01 <= R' <= 99.99
All output values should be printed upto 2 decimal places.
The output will be invalid in the following cases-

The input ranges or conditions are not satisfied.
The ranges of calculated values are not satisfied.
The relation between CSV and CR is not satisfied
Example
Input:

4
25000
35
5
85
6
20000
19
2
60
3
25658
520
510
65
3
22000
30
-5
46
6
Output:

30.00
79.00
750000.00
375000.00
296250.00
Invalid Input
Invalid Input
Invalid Input


'''


for _ in range(int(input())):
    n=int(input())
    sv=float(input())
    csv=float(input())
    r=float(input())
    cr=float(input())
    if(n<=10000000) and n>=20000 and sv>=20.00 and sv<=10000.00 and csv>=-2000.00 and csv<=2000.00 and r>=0.01 and r<=99.99 and cr>=-10.00 and cr<=10.00:
        sv1=sv-csv
        r1=r-cr
        cv=n*min(sv,sv1)
        ce=cv*50/100
        ca=ce*min(r,r1)/100
        sv1 = round(sv1 * 100) / 100
        r1 = round(r1 * 100) / 100
        cv = round(cv * 100) / 100
        ce = round(ce * 100) / 100
        ca = round(ca * 100) / 100
        if(sv1>=20.00 and sv1<=10000.00 and r1>=0.01 and r1<=99.99)and((csv<0 and cr<=0) or(csv>=0)):
            print('{0:.2f}'.format(sv1))
            print('{0:.2f}'.format(r1))
            print('{0:.2f}'.format(cv))
            print('{0:.2f}'.format(ce))
            print('{0:.2f}'.format(ca))
        else:
            print('Invalid Input')
    else:
        print('Invalid Input')

