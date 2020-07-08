'''
Power Outage
In a remote location, a student is watching a game of ODI cricket on TV. At some point, power goes off; the student is assured about the current run rate of the batting team, which batsman is on strike and individual scores of both the batsmen playing currently but is unsure of exact number of runs the batting team has scored. After some time, power is restored for a moment and at that point in time, a Timeline of runs scored in last D no. of deliveries and current run rate is being shown on TV. Exactly D no. of deliveries were bowled in between the power outage.

Given these details, you need to find out the total number of runs scored by the team and score of batsmen currently playing.

Wickets falling will be shown as W. Assume batsmen can only be 'bowled' in these D deliveries
Consequent overs are bowled from opposite ends. (ie. batsmen change sides at the end of an over)
Constraints
Runs scored per delivery can be between 0 and 6
No extra deliveries are bowled and no extra runs scored (Leg byes, No balls, etc.)
Number of deliveries D < 50
RR1 is not equal to RR2
Number of wickets falling in the timeline < 10
Input Format
First line will provide the run rate at first instance RR1
Second line will provide Batsmen scores, space separated (striker's score will be given first)
Third line will provide space separated list of runs scored in D deliveries
Fourth line will provide the run rate at second instance RR2
Output
Space separated values of Total Runs, Striker, Non-Striker at the second instance (after Timeline). Consider side change if an over is completed at the end of the timeline.

Example Input
9
21 13
1 1 1 1 1 0 0 0 0 4 2 0 0 1 6 0 1 1 0 0
8.3182
Output
122 20 34
Explanation
Assuming number of deliveries bowled at the first instance is b and number of runs scored is r
Solving for these we will get b=68 and r=102. So current run score will be 102+20 = 122
We also get that 4 deliveries remained in the 'Over' when the power goes off (an 'Over' consists of 6 consecutive deliveries bowled from one end). So adding the runs individually to batsmen scores we get current scores as 20 and 34.
Example Input 2
9
21 13
1 1 1 1 1 0 0 0 0 4 2 0 0 1 6 0 1 1 0 W
8.3182
Output
122 0 34
Explanation
Here wicket goes does at the last ball. Hence, the striker, who is the new batsman, has zero runs.
'''


rr1=float(input())
B1,B2=list(map(int,input().split()))
a=list(input().split())
rr2=float(input())
s=0
b=len(a)
#rr1=totalscore/totalovers --> rr1=totalscore/(totalballs/6)-->rr1=6*totalscore/totalballs
#rr2=(totalscore+s)*6/(totalballs+b) from above totalscore=rr1*totalballs/6 sub in rr2
#rr2=(rr1*totalballs+6s)/(totalballs+b)--> rr2*totalballs+rr2*b=rr1*totalballs+6s
#-->rr2*b-6s=totalballs(rr1-rr2) --> totalballs=(rr2*b-6s)/(rr2-rr1)
#totalscore=(rr1*totalballs)/6
for i in range(b):
    if a[i]!='W':
        s=s+int(a[i])
totalb=round((rr2*b-6*s)/(rr1-rr2))
totalr=round(totalb*rr1/6)
#print(totalb,totalr)
for i in range(b):
    if a[i]!='W':
        B1=B1+int(a[i])
        #print(B1)
        if int(a[i])%2==1: #if score is odd num-- swap the batsmen
            temp=B1
            B1=B2
            B2=temp
    else:
        B1=0
    totalb+=1
    #print('balls',totalb)
    if totalb%6==0: #if over is up-- swap the batsmen
        temp=B1
        B1=B2
        B2=temp
print(totalr+s,B1,B2)
