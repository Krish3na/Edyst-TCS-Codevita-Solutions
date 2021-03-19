'''
CodeVita 2016, Calculate Salary and PF
Calculate Salary and PF
Calculate the Final Salary & Final Accumulated PF of an Employee working in ABC Company Pvt. Ltd.

The Company gives two Increments (i.e. Financial Year Increment & Anniversary Increment) to an Employee in a Particular Year.

The Employee must have Completed 1 Year to be Eligible for the Financial Year Increment. The Employee who are joining in the month of Financial Year Change (i.e. April) are considered as the Luckiest Employees, because after completion of 1 Year, they get Two Increments (Financial Year Increment & Anniversary Increment).

Rate of Interest for the Financial Year Increment = 11%.
Rate of Interest for the Anniversary Increment = 12%.

From 4th Year, the Financial Year Increment will be revised to 9%.
From 8th Year, the Financial Year Increment will be revised to 6%.
The Company is giving special Increment for the Employee who have completed 4 years & 8 years respectively.

So, the Anniversary Increment of the Employee for the 4th Year will be 20% and the Anniversary Increment of the Employee for the 8th year will be 15%.

Calculate the Final Salary after N number of Years as well as Calculate the Accumulated PF of the Employee after N number of Years.

Please Note that, the Rate of Interest for calculating PF for a Particular Month is 12%.

Moreover, take the upper Limit of the amount if it is in decimal (For e.g. - If any Amount turns out to be 1250.02, take 1251 for printing the result.)

Input Format:
First line contains k, the number of inputs. Following k lines contain:

Joining Date in dd/mm/yy format
Current CTC
Number of Years for PF & Salary Calculation.
Output Format:
Salary after the Specified Number of Years (i.e. CTC after N number of Years) in the following format
Final Salary =
Accumulated PF of the Employee after N number of Years in the following format
Final Accumulated PF =

Constraints:
Calculation should be done up to 11 digit precision and output should be printed with ceil value

Sample Input & Output:
Input:

1
01/01/2016
10000
2
Output:

Final Salary = 13924
Final Accumulated PF = 2655
Input:

1
19/01/2016
6500
4
Output:

Final Salary = 14718
Final Accumulated PF = 4343

'''
