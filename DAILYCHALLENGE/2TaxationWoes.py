'''

Taxation Woes
In a country, there are N slabs for Income tax which are common for all age groups and genders. As an income tax officer, investigating a case, you have the amount of tax paid by each employee of an organization.

Considering the income tax slabs and rebates offered, you need to find the total amount paid by the organization in salaries to the employees to match it with the amount reported by the organization in its filed Income tax Returns.

Information regarding the income tax slabs, rebate amount and the income tax paid by each employee of the organization will be provided.

Rebate amount is subtracted from the total salary of each employee. Tax is calculated on the remaining amount. You need to calculate the sum of total salary paid to the employees in that year.

Constraints
Number of tax slabs = Number of percentage on tax slabs
0<= Rebate, tax paid, slab <=1000000
Input Format
First Line will provide the Amount in each slab, separate by space (' ')
Second Line will provide the percentage of tax applied on each slab. Number of values in this line will be same as that in line one, separate by space (' ')
Third Line will provide the Rebate considered
Fourth line will provide the tax paid by each employee, separate by space (' ')
Output
Total Salary paid by the organization to its employees
Example Input
300000 600000 900000
10 20 30
100000
90000 150000 210000 300000
Output
5300000
Explanation
Slabs and tax percentage indicate that for salary:

Between 0 - 300000, tax is 0%
Between 300001 - 600000, tax is 10%
Between 600001 - 900000, tax is 20%
Greater than 900001, tax is 30%
First, we exclude the rebate from the salary of each employee. This will be the taxable component of salary. Upon, taxable salary apply the slab and tax percentage logic. Upon computation, one finds that employees are paid amounts 1000000, 1200000, 1400000, 1700000 respectively, as salaries. So, the total salary paid to all employees in that year will be 5300000.

Hint: - It may be helpful to browse the internet to know general rules regarding income tax calculations.
'''


slabs=list(map(int,input().strip().split()))
taxrates=list(map(int,input().strip().split()))
rebate=int(input())
taxespaid=list(map(int,input().strip().split()))
num_employees=len(taxespaid)
salaries=[0]*num_employees
for i in range(num_employees):
    curr_emppaid=taxespaid[i]
    #print(curr_emp)
    salaries[i]+=slabs[0]
    for j in range(1,len(slabs)):
        max_curr_slab=taxrates[j-1]*(slabs[j]-slabs[j-1])/100
        if max_curr_slab<=curr_emppaid:
            salaries[i]+=(slabs[j]-slabs[j-1])
            curr_emppaid-=max_curr_slab
        else:
            paid_in_slab=(curr_emppaid*100)/taxrates[j-1]
            salaries[i]+= paid_in_slab
            curr_emppaid-= curr_emppaid
    if curr_emppaid>0:
        salaries[i]+= ((curr_emppaid*100)/taxrates[-1])
    salaries[i]+=rebate
    
print(int(sum(salaries)))
