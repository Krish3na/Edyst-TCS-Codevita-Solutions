from itertools import combinations
t=int(input())
def summ(l):
    res=0
    for i in l:
        res+=i
    return res
def combi(ll,p):
    cnt=0
    for l in ll:
        if len(l)>=2:
            added=summ(l)
            if added>=p:
                cnt+=1
    return cnt

def sub_lists(my_list):
	subs = []
	for i in range(0, len(my_list)+1):
	  temp = [list(x) for x in combinations(my_list, i)]
	  if len(temp)>0:
	    subs.extend(temp)
	return subs

for i in range(t):
    m, p=map(int,input().split())
    l=list(map(int,input().split()))
    ll=sub_lists(l)
    tcombi=combi(ll,p)
    print(tcombi)
