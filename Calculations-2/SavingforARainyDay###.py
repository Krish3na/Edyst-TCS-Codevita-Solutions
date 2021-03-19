'''

CodeVita 2016, Saving for a rainy day
Saving for a Rainy Day
By nature, an average Indian believes in saving money. Some reports suggest that an average Indian manages to save approximately 30+% of his salary. Dhaniram is one such hard working fellow. With a view of future expenses, Dhaniram resolves to save a certain amount in order to meet his cash flow demands in the future.

Consider the following example.

Dhaniram wants to buy a TV. He needs to pay Rs 2000/- per month for 12 installments to own the TV. If, let’s say, he gets 4% interest per annum on his savings bank account, then Dhaniram will need to deposit a certain amount in the bank today, such that he is able to withdraw Rs 2000/- per month for the next 12 months without requiring any additional deposits throughout.

Your task is to find out how much Dhaniram should deposit today so that he gets assured cash flows for a fixed period in the future, given the rate of interest at which his money will grow during this period.

Input Format:
First line contains k, the number of inputs. The following k lines have:

First line contains desired cash flow M
Second line contains period in months denoted by T
Third line contains rate per annum R expressed in percentage at which deposited amount will grow
Output Format:
Print total amount of money to be deposited now rounded off to the nearest integer

Constraints:
M > 0
T > 0
R >= 0
Calculation should be done upto 11-digit precision

Example
Input:

k = 3
 
500
3
12
 
6000
3
5.9
 
500
2
0	
Output:

1470
17824
1000


'''

for _ in range(int(input())):
    monthlypay=int(input())
    months=int(input())
    rateofinterest=float(input())
    requiredamt=float(monthlypay)
    while(months!=0):
        amt=requiredamt/(1+rateofinterest/1200)
        interest=requiredamt-amt
        requiredamt+=(monthlypay-interest)
        months=months-1
    requiredamt-=monthlypay
    k=round(requiredamt)
    print(k)

