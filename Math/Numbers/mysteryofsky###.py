'''
CodeVita 2016, Mystery of Sky
Mystery of Sky
Stark is a 10 year old kid and he loves stars. So, he decided every day he will capture a picture of a sky. After doing this for many days he found very interesting observations.

Every day the total number of stars in the sky is same as days completed for a calendar year. He noticed, on Saturday’s and Sunday’s that there are no stars in the sky. Stark’s camera does not have wide angle capture feature so he could only capture maximum of 50 stars at a time. So, he assumed that there are only 50 stars in the sky that day. Also, the camera discharges every 4th day and he is not be able to click any picture that day. So let’s say, if the first day of calendar (01/01/0001) starts on a Monday then on Thursday he can’t click any pictures. Then resuming on Friday he can take pictures until Sunday, but can’t take picture on Monday, followed by downtime on Friday, then Tuesday, then Saturday etc. When the camera discharges he considers 0 stars that day.

You are his programmer friend and want to help him. You need to write a code which will tell him on a particular date how many stars Stark’s camera was able to click.

You can assume Stark has an ancient camera and your first input will be the day for date (01/01/0001) and then followed by any date on which Stark wants to find out the number of stars in the sky.

Input Format:
Every line of input will contain a Day at date 01/01/0001 in dd/mm/yyyy format followed by a Date in the same format (on which we have to count the stars)

Output Format:
For valid Input:
Count of the number of stars in the sky on the given date

For Invalid Input:
Print “Invalid Date” for invalid date

Print “Invalid Day” for invalid day

Sample Input / Output
Input
Monday
30/02/1990

Output
Invalid Date

Input
Thursday

Output
Invalid Day

Input
Wednesday
24/01/2056

Output
24

Explanation
Its 24th day of the year and neither is Saturday/Sunday nor has the camera discharged on this day.
'''


import datetime
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
def date_validation(day, month, year): 
    valid=True
    try : 
        datetime.datetime(int(year),int(month), int(day))
    except ValueError : 
        valid= False
    return valid
def countLeapYears(d,m,y): 
    years = y
    if (m <= 2) : 
        years-= 1
    return int(years / 4 - years / 100 + years / 400 ) 
def getDifference(d1,m1,y1,d2,m2,y2): 
    n1 = y1 * 365 + d1 
    for i in range(0, m1 - 1): 
        n1 += monthDays[i]
    n1 += countLeapYears(d1,m1,y1)
    n2 = y2 * 365 + d2 
    for i in range(0, m2 - 1): 
        n2 += monthDays[i]  
    n2 += countLeapYears(d2,m2,y2)
    return (n2 - n1)
d1,m1,y1=1,1,1
day=input()
try:
    d2,m2,y2=map(int,input().split('/'))
    if(not date_validation(d2,m2,y2)):
        print("Invalid Date")
    else:
        n=getDifference(d1,m1,y1,d2,m2,y2)
        days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        ind=days.index(day)
        if(n%4==3 or (ind+n)%7==5 or (ind+n)%7==6):
            print(0)
        else:
            n=getDifference(0,1,y2,d2,m2,y2)
            print(min(n,50))
except:
    print("Invalid Day")


####My code flopped
'''
days_week={"Saturday":0,"Sunday":1,"Monday":2,"Tuesday":3,"Wednesday":4,"Thursday":5,"Friday":6}
days_month=[31,28,31,30,31,30,31,31,30,31,30,31]

def leapyears(year):
    leap=0
    nonleap=0
    for y in range(1,year+1):
        if (y % 4 == 0 and y % 100 != 0) or (y % 100 == 0 and y % 400 == 0):
            leap+=1
        else:
            nonleap+=1
    return nonleap,leap

def isleap(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 100 == 0 and y % 400 == 0):
        return 1
    else:
        return 0   
    
def noOfdays(date):
    ref_date=[1,1,1]
    pyear=date[2]
    pmonth=date[1]
    pday=date[0]
    nonleap, leap = leapyears(pyear-1)
    print(nonleap,leap)
    noofdays = 365*nonleap + 366*leap
    for i in range(pmonth-1):
        noofdays+=days_month[i]
    noofdays+=pday
    
    if isleap(pyear):
        if pmonth>2:
            noofdays+=1
        if pmonth==2:
            if pday==29:
                noofdays+=1
    
    return noofdays

try:
    day=input()
    date=list(map(int,input().split('/')))
    day_idx = days_week[day]
    if date[0]>=29 and date[1]==2:
        if isleap(date[2])==0:
            print('Invalid Date')
            exit(0)
    
except:
    print('Invalid Day')
    
noofdays = noOfdays(date)
if (day_idx + noofdays)%7 == 0 or (day_idx + noofdays)%7 == 1:
    print(0)
    exit(0)
if (noofdays - 1) % 4 == 3:
    print(0)
    exit(0)
print(min(noofdays,50))


'''
