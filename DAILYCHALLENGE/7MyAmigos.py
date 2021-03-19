'''

My Amigos
2N friends (A, B, C ... 2N) are standing in a circle. There is exactly one person standing opposite of one other person. Some of them are facing inwards and some of them are facing outwards. Here given some facts your task is to build the standing positions and answer a few Questions. If the arrangement is not possible or more than one arrangement is possible, then print ARRANGEMENT NOT POSSIBLE

The formats of Facts & Questions and its meanings are as follows.

Facts

1AB means : A and B are standing adjacent to each other
2AB means : A and B are standing opposite to each other
3AB means : A is standing to the immediate left of B
4AB means : A is standing to the immediate right of B
5A means : A is facing inwards
6A means : A is facing outwards
7n means : n people are facing inwards, where n is a number
8n means : n people are facing outwards, where n is a number
Questions

?2A means : who is standing opposite of A?
?3A means : who is standing to the immediate left of A?
?4A means : who is standing to the immediate right of A?
?5A means : is A facing inwards? Ans: Y/N
?6A means : is A facing outwards? Ans: Y/N
Constraints
1 < N < 10
1 < Total Facts < 30
1 < Total Questions < 20
Input Format
First line contains N
Then multiple facts, separated by semicolon
Then multiple questions, separated by semicolon
Output
Answers, separated by semicolon corresponding to order of questions OR ARRANGEMENT NOT POSSIBLE

Example Input 1
2 
2AB;72;1AC;6D;4BD;6C
?2D;?3C;?4B;?5A;?6B
Output
C;B;D;Y;N
Explanation
4 people- A, B, C and D are standing in circle.
There are 6 facts separated in semicolons:

2AB ==> A and B are standing opposite
72 ==> 2 people are facing inwards
1AC ==> A and C are standing nearby
6D ==> D is facing outwards
4BD ==> B is standing immediate right of D
6C ==> C is facing outwards
From the above facts, we can build the standing positions as below image:

There are 5 questions:

?2D ==> who is standing opposite of D? Ans: C
?3C ==> who is standing immediate left of C? Ans: B
?4B ==> who is standing immediate right of B? Ans: D
?5A ==> is A facing inwards? Ans: Y
?6B ==> is B facing outwards? Ans: N
Finally printing all answers in a single line separated by semicolon.

Example Input
2
4BA;3CA;3CD;5C;5B
?5A;?3D;?4C;?6B
Output
ARRANGEMENT NOT POSSIBLE
Explanation
We can arrange 4 people in two different ways as the image below, from the facts provided. Directions of A and D can be set differently.



'''

def copy_arr(arr):
    duplicate = []
    for i in arr:
        duplicate.append(i)
    return duplicate

def is_adjacent(person1, person2, p):
    p1_index = p.index(person1)
    p2_index = p.index(person2)
    if abs(p1_index - p2_index) == 1:
        return True
    if p2_index == len(p)-1 and p1_index == 0:
        return True
    if p1_index == len(p)-1 and p2_index == 1:
        return True
    return False

def place_adjacent(person1, person2, possibilities, directions):
    new_possibilities = []
    for curr in possibilities:
        if person1 in curr and person2 in curr: # if they already exist, just confirm adjacency
            if is_adjacent(person1, person2, curr):
                new_possibilities.append(curr)
        elif person1 in curr or person2 in curr:# if either doesn't exist
            me = person1
            other = person2
            if person1 not in curr:
                me,other = other, me
            me_index = curr.index(me)
            other_index_1 = (curr.index(me) + 1)%len(curr)
            other_index_2 = (curr.index(me) - 1)%len(curr)
            for i in [other_index_1, other_index_2]:
                if curr[i] == '':
                    new_p = copy_arr(curr)
                    new_p[i] = other
                    new_possibilities.append(new_p)
        else:
            # go through all the vacant spaces and keep adjacent pairs
            me = person1
            other = person2
            for i in range(len(curr)):
                next_index = (i+1)%len(curr)
                if curr[i] == '' and curr[next_index] == '':
                    ## add possibility of a,b
                    
                    new_p = copy_arr(curr)
                    new_p[i] = me
                    new_p[next_index] = other
                    new_possibilities.append(new_p)

                    ## add possibility of b,a

                    new_p = copy_arr(curr)
                    new_p[i] = other
                    new_p[next_index] = me
                    new_possibilities.append(new_p)


    return new_possibilities

def place_opposite(person1, person2, possibilities, directions):
    new_possibilities = []
    for curr in possibilities:
        if person1 in curr and person2 in curr: # if they already exist, just confirm opposite
            if abs(curr.index(person1) - curr.index(person2)) == len(curr)//2:
                new_possibilities.append(curr)
        elif person1 in curr or person2 in curr:# if either doesn't exist
            me = person1
            other = person2
            if person1 not in curr:
                me,other = other, me
            me_index = curr.index(me)
            other_index = (curr.index(me) + (len(curr)//2))%len(curr)
            if curr[other_index] == '':
                new_p = copy_arr(curr)
                new_p[other_index] = other
                new_possibilities.append(new_p)
        else:
            # go through all the vacant spaces and keep opposite pairs
            me = person1
            other = person2
            for i in range(len(curr)):
                next_index = (i+(len(curr)//2))%len(curr)
                if curr[i] == '' and curr[next_index] == '':
                    ## add possibility of a,b
                    
                    new_p = copy_arr(curr)
                    new_p[i] = me
                    new_p[next_index] = other
                    new_possibilities.append(new_p)

                    ## add possibility of b,a

                    new_p = copy_arr(curr)
                    new_p[i] = other
                    new_p[next_index] = me
                    new_possibilities.append(new_p)


    return new_possibilities


# facing up is inward, facing down is outward
def place_left(person1, person2, possibilities, directions):
    # person1 left, person2 right
    new_possibilities = []
    if person2 not in directions:
        new_possibilities = place_adjacent(person1, person2,possibilities, directions)
        return new_possibilities
    for curr in possibilities:
        if person2 in curr:
            me = curr.index(person2)
            if directions[person2] == 'in':
                other = (curr.index(person2) - 1)%len(curr)
            elif directions[person2] == 'out':
                other = (curr.index(person2) + 1)%len(curr)            
            
            if curr[other] != '':
                continue
            new_p = copy_arr(curr)
            new_p[other] = person1
            new_possibilities.append(new_p)
        elif person1 in curr:
            other = curr.index(person1)
            if directions[person2] == 'in':
                me = (other + 1)%len(curr)
            elif directions[person2] == 'out':
                me = (other - 1)%len(curr)         
            
            if curr[me] != '':
                continue
            new_p = copy_arr(curr)
            new_p[me] = person2
            new_possibilities.append(new_p)
        else:
            for i in range(len(curr)):
                if directions[person2] == 'in':
                    other = (i - 1)%len(curr)
                elif directions[person2] == 'out':
                    other = (i + 1)%len(curr)   
                if curr[i] != '' or curr[other] != '':
                    continue
                me = i
                new_p = copy_arr(curr)
                new_p[me] = person2
                new_p[other] = person1
                new_possibilities.append(new_p)
    
    return new_possibilities




# facing up is inward, facing down is outward
def place_right(person1, person2, possibilities, directions):
    # person1 right, person2 left
    new_possibilities = []
    if person2 not in directions:
        new_possibilities = place_adjacent(person1, person2,possibilities, directions)
        return new_possibilities
    for curr in possibilities:
        if person2 in curr:
            me = curr.index(person2)
            if directions[person2] == 'in':
                other = (curr.index(person2) + 1)%len(curr)
            elif directions[person2] == 'out':
                other = (curr.index(person2) - 1)%len(curr)            
            
            
            if curr[other] == person1:
                new_p = copy_arr(curr)
                new_p[other] = person1
                new_possibilities.append(new_p)
            if curr[other] != '':
                continue

            new_p = copy_arr(curr)
            new_p[other] = person1
            new_possibilities.append(new_p)
        elif person1 in curr:
            other = curr.index(person1)
            if directions[person2] == 'in':
                me = (other - 1)%len(curr)
            elif directions[person2] == 'out':
                me = (other + 1)%len(curr)         
            
            if curr[me] != '':
                continue

            new_p = copy_arr(curr)
            new_p[me] = person2
            new_possibilities.append(new_p)
        else:
            for i in range(len(curr)):
                if directions[person2] == 'in':
                    other = (i + 1)%len(curr)
                elif directions[person2] == 'out':
                    other = (i - 1)%len(curr)     
                if curr[i] != '' or curr[other] != '':
                    continue
                me = i
                new_p = copy_arr(curr)
                new_p[me] = person2
                new_p[other] = person1
                new_possibilities.append(new_p)
    
    return new_possibilities



N = int(input())
N = 2*N

facts = input().split(';')
questions = input().split(';')

arrangement = [''] * N

possibilities = []
total_inwards = 0
total_outwards = 0
inward_known = 0
outward_known = 0
positional_facts = []
directions = {}

for fact in facts:
    if fact[0] == '7':
        total_inwards = int(fact[1])
        total_outwards = N - total_inwards
    elif fact[0] == '8':
        total_outwards = int(fact[1])
        total_inwards = N - total_outwards
    elif fact[0] == '5':
        directions[fact[1]] = "in"
        inward_known+= 1
    elif fact[0] == '6':
        directions[fact[1]] = "out"
        outward_known+=1
    else:
        positional_facts.append(fact)

positional_facts.sort(key = lambda x: min(x[1:]))

alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if inward_known == total_inwards:
    for i in range(N):
        if alphas[i] not in directions:
            directions[alphas[i]] = "out"
            outward_known+=1

if outward_known == total_outwards:
    for i in range(N):
        if alphas[i] not in directions:
            directions[alphas[i]] = "in"
            inward_known+=1
        

# print(positional_facts)

arrangement[0] = min(positional_facts[0][1:])
possibilities.append(arrangement)

# print(arrangement)
# print(directions)

for fact in positional_facts:
    info = fact[0]
    # print(fact)
    if info == '1':
        possibilities = place_adjacent(fact[1], fact[2], possibilities, directions)
    if info == '2':
        possibilities = place_opposite(fact[1], fact[2], possibilities, directions)
    if info == '3':
        possibilities = place_left(fact[1], fact[2], possibilities, directions)
    if info == '4':
        possibilities = place_right(fact[1], fact[2], possibilities, directions)
    
    # if len(possibilities) == 0:
    #     break
    # print(possibilities)

if len(possibilities) != 1:
    print('ARRANGEMENT NOT POSSIBLE')
else:
    arrangement = possibilities[0]
    # print(arrangement)
    for  index in range(len(questions)):
        q = questions[index]
        query = int(q[1])
        val = q[2]
        if query == 2:
            me = arrangement.index(val)
            other = (me+ (len(arrangement)//2))%len(arrangement)
            ans = arrangement[other]
        if query == 3:
            me = arrangement.index(val)
            dir = directions[val]
            if dir == 'out':
                other = (me+1 )%len(arrangement)
            if dir == 'in':
                other = (me-1) %len(arrangement)
            ans = arrangement[other]
        if query == 4:
            me = arrangement.index(val)
            dir = directions[val]
            if dir == 'out':
                other = (me-1) %len(arrangement)
            if dir == 'in':
                other = (me+1) %len(arrangement)
            ans = arrangement[other]
        if query == 5:
            dir = directions[val]
            if dir == 'in':
                ans = 'Y'
            else:
                ans = 'N'
        if query ==6:
            dir = directions[val]
            if dir == 'out':
                ans = 'Y'
            else:
                ans = 'N'
        if index < len(questions)-1:
            print(ans,end=';')
        else:
            print(ans)
        
#######################################################################

##OR
'''
def search(s,l1):
    for i in range(len(s)):
        for j in range(len(l1)):
            if s[i] in l1[j] and s[i]!='':
                return l1[j]
    return ""
 
def empty(e):
    for i in range(len(e)):
        if e[i]!='':
            return False
    return True
n=int(input())
l=list(map(str,input().split(";")))
f=True
for i in range(len(l)):
    if '7' in l[i] or '8' in l[i]:
        f=False
        break
q=list(map(str,input().split(";")))
l.sort(reverse=True)
l1=[]
l2=[]
for i in range(len(l)):
    if(len(l[i])==3):
        l1.append(l[i])
    else:
        l2.append(l[i])
s=['']*(2*n)
 
while(len(l1)!=0):
    if(empty(s)):
        t=l1[0]
        del(l1[0])
        if t[0]=='4':
            s[0]=t[2]
            s[1]=t[1]
        elif(t[0]=='3'):
            s[0]=t[1]
            s[1]=t[2]
    else:
        t=search(s,l1)
        if(t!=''):
            inde=l1.index(t)
            del(l1[inde])
            
        else:
            f=True
            break
            
        if t[1] in s:
            ind=s.index(t[1])
            if t[0]=='4':
                if ind==0:
                    s[-1]=t[2]
                else:
                    s[ind-1]=t[2]
            elif(t[0]=='3'):
                if(ind==len(s)-1):
                    s[0]=t[2]
                else:
                    s[ind+1]=t[2]
            elif(t[0]=='2'):
                for j in range(n):
                    ind+=1
                    if(ind==len(s)):
                        ind=0
                s[ind]=t[2]
            elif(t[0]=='1'):
                if(ind==0):
                    if(s[1]==''):
                        s[1]=t[2]
                    else:
                        s[-1]=t[2]
                elif(ind==len(s)-1):
                    if(s[-2]==''):
                        s[-2]=t[2]
                    else:
                        s[0]=t[2]
                else:
                    if(s[ind-1]==''):
                        s[ind-1]=t[2]
                    else:
                        s[ind+1]=t[2]
        else:
            ind=s.index(t[2])
            if t[0]=='4':
                if ind==len(s)-1:
                    s[0]=t[1]
                else:
                    s[ind+1]=t[1]
            elif(t[0]=='3'):
                if(ind==0):
                    s[-1]=t[1]
                else:
                    s[ind-1]=t[1]
            elif(t[0]=='2'):
                for j in range(n):
                    ind+=1
                    if(ind==len(s)):
                        ind=0
                s[ind]=t[1]
            elif(t[0]=='1'):
                if(ind==0):
                    if(s[1]==''):
                        s[1]=t[1]
                    else:
                        s[-1]=t[1]
                elif(ind==len(s)-1):
                    if(s[-2]==''):
                        s[-2]=t[1]
                    else:
                        s[0]=t[1]
                else:
                    if(s[ind+1]==''):
                        s[ind+1]=t[1]
                    else:
                        s[ind-1]=t[1]
    #print(s)
if(f):
    print("ARRANGEMENT NOT POSSIBLE")
else:
    d=['']*(2*n)
    l2.sort()
    c=0
    inw=False
    out=False
    for i in range(len(l2)):
        if(l2[i][1].isdigit()==False):
            ind=s.index(l2[i][1])
            if(l2[i][0]=='5'):
                d[ind]='i'
            elif(l2[i][0]=='6'):
                d[ind]='o'
        else:
            c=int(l2[i][1])
            if(l2[i][0]=='7'):
                inw=True
            else:
                out=True
            break
    ci=d.count('i')
    co=d.count('o')
    if(inw):
        if(c!=ci):
            for i in range(len(d)):
                if(d[i]==''):
                    d[i]='i'
        else:
            for i in range(len(d)):
                if(d[i]==''):
                    d[i]='o'
    else:
        if(c!=co):
            for i in range(len(d)):
                if(d[i]==''):
                    d[i]='o'
        else:
            for i in range(len(d)):
                if(d[i]==''):
                    d[i]='i'
    re=[]
    #int(str(d))
    for i in range(len(q)):
        if(q[i][1]=='2'):
            ind=s.index(q[i][2])
            for j in range(n):
                ind+=1
                if(ind==len(s)):
                    ind=0
            re.append(s[ind])
        elif(q[i][1]=='3'):
            ind=s.index(q[i][2])
            if(ind==0):
                if(d[ind]=='o'):
                    re.append(s[-1])
                else:
                    re.append(s[1])
            else:
                if(d[ind]=='o'):
                    re.append(s[ind-1])
                else:
                    if(ind==len(s)-1):
                        re.append(s[0])
                    else:
                        re.append(s[ind+1])
        elif(q[i][1]=='4'):
            ind=s.index(q[i][2])
            if(ind==len(s)-1):
                if(d[ind]=='o'):
                    re.append(s[0])
                else:
                    re.append(s[-2])
            else:
                if(d[ind]=='o'):
                    re.append(s[ind+1])
                else:
                    if(ind==0):
                        re.append(s[-1])
                    else:
                        re.append(s[ind-1])
        elif(q[i][1]=='5'):
            ind=s.index(q[i][2])
            if(d[ind]=='i'):
                re.append('Y')
            else:
                re.append('N')
        elif(q[i][1]=='6'):
            ind=s.index(q[i][2])
            if(d[ind]=='o'):
                re.append('Y')
            else:
                re.append('N')
    #print(d)
    #print(s)
    for i in range(len(re)-1):
        print(re[i],end=";")
    print(re[-1])

'''
