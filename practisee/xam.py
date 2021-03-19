import operator
'''
import math
l=list(map(int,input().split()))
l=[0]+l
mat=[]
matt=[['*']*7 for i in range(7)]
i=1
while i<=7:
    nwl=l[i:i+3]
    mat.append(nwl)
    i=i+3
matt[0][0]=mat[0][0]
for i in range(2):
    for j in range(2):
        gcd1=math.gcd(mat[i][j],mat[i][j+1])
        gcd2=math.gcd(mat[i][j],mat[i+1][j])
        gcd3=math.gcd(mat[i][j],mat[i+1][j+1])
        #print(gcd1,gcd2,gcd3)
        if gcd1==1 and j==0:
            matt[i][j+1]=mat[i][j+1]
        else:
            matt[i][j+2]=mat[i][j+1]
        if gcd2==1 and j==0:
            matt[i+1][j]=mat[i+1][j]
        else:
            matt[i+2][j]=mat[i+1][j]
        
            
for i in range(len(matt)):
    for j in range(len(matt)):
        print(matt[i][j],end=' ')

    print()


def maximum_profit(no_stocks,stocks_limit,total_amount,stock_costs,stock_profits,c,max_profit):
  
    max_val_profits=dic[-1][1]
    max_ind=stock_profits.index(max(stock_profits))
    max_val_profits=dic[-1][1]
    max_ind=stock_profits.index(max_val_profits)
    #print(max_ind)
    max_val_stocks=stock_costs[max_ind]
    #print(max_val)
    for i in range(stocks_limit):
        if total_amount > c and  total_amount >= c + max_val_stocks:
            c += max_val_stocks
            max_profit += ((max_val_stocks*stock_profits[max_ind])/100)
                    
        else:
            print(int(max_profit),end='')
            return max_profit
    
    for i in range(stocks_limit):
        if not (total_amount < c + max_val_stocks):
            if not (total_amount<= c):
                    max_profit += dp[max_val_stocks]
                    c += max_val_stocks
        else:
            print(int(max_profit),end='')
            #dp[stock_profits[max_ind]]=max_profit
            return max_profit
          
    stock_costs.pop(max_ind)
    stock_profits.pop(max_ind)
    dic.pop(-1)
    #print(int(max_profit))
    #print(dp)
    maximum_profit(no_stocks,stocks_limit,total_amount,stock_costs,stock_profits,c,max_profit)

no_stocks,stocks_limit,total_amount=map(int,input().split())
stock_costs=list(map(float,input().split()))
stock_profits=list(map(float,input().split()))
max_profit=0
c=0
dic=dict(zip(stock_costs,stock_profits))
dic = sorted(dic.items(), key=operator.itemgetter(1))
#print(dic)
dp={}
for i in range(no_stocks):
    dp[stock_costs[i]]=stock_costs[i]*stock_profits[i]/100
#print(dp)
maximum_profit(no_stocks,stocks_limit,total_amount,stock_costs,stock_profits,c,max_profit)
#print(maximum_profit)


p=input("")
q=input("")
p=list(p.split(" "))
q=list(q.split(" "))
for t in range(0,len(q)-1):
    c=[0 for i in range(t,len(q))]
    for i in p:
        for j in range(len(q)):
            k=0
while(k):
    m2=c.index(m1)
    for i in range(m2,len(c)):
        if(c[i]==m1):
            if(ord(q[i])<ord(q[m2])):
                m2=i
        else:
            m2=c.index(m1)
        q[m2],q[t]=q[t],q[m2]
print("".join(q))

n=int(input())
steps=0
while n>0:
    if n%5==0:
        steps+=1
        n=n-5
    elif n%4==0:
        steps+=1
        n=n-4
    elif n%3==0:
        steps+=1
        n=n-3
    elif n%2==0:
        steps+=1
        n=n-2
    elif n%1==0:
        steps+=1
        n=n-1

print(steps)
#inputs
9
34 54 65 76 88 23 56 76 43
7
1 3
2 3
1 2
6 8
5 4
5 7
8 9

5
23 43 123 54 2
3
1 3
2 3
1 2


        
'''
# Max funds
n=int(input())
funds=list(map(int,input().split()))
n_pairs=int(input())
pairs=[]
groups=[]
for i in range(n_pairs):
    
    a,b=map(int,input().split())
    #print(a,b)
    if len(groups)==0:
        groups.append([a,b])
    elif len(groups)!=0:
        for j in range(len(groups)) :
            if (a in groups[j])or (b in groups[j]):
                groups[j].append(b)
                groups[j].append(a)
                groups[j]=sorted(list(set(groups[j])))
                #print('if')
                break
            else:
                if j==len(groups)-1:
                    groups.append([a,b])
                    #print('else',groups)
final=[]    
for l in groups:
    summ=0
    for i in l:
        summ+=funds[i-1]
    final.append(summ)

print(max(final),end='')
