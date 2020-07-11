'''

Admin Blues
A person, new to his job in a start-up, was given a task by his supervisor to prepare a
report where the user IDs (of all the employees) is a part of the report. He fetched the
user IDs from database and then used a spreadsheet function to concatenate them to
share it in email as text. However, while concatenating, he forgot to put a comma ,
in between the two user IDs
As a rule, user IDs of the portal should be minimum 4 characters and can only contain alphabets and cannot start or end with a vowel.

Supervisor knows about this rule and the number of employees in the department. Therefore, he tries to guess a possible set of user IDs from the given string (of user IDs in the email). You need to find the total no. of different set of user Ids that are possible given the number of employees in the department and the string of user IDs.

Constraints
1<Number of Employees<10
7<Length of user id string <51
Input Format
First Line contains an integer, which provides the Number of Employees in the
organization
Second Line contains a string of concatenated user ids
Output
Number of possibilities of user ID sets
If none are possible, print 0
Example Input 1
2
nonajklop
Output
1
Explanation
Since supervisor knows there are only 2 user IDs and they cannot start or end with a
vowel, there is only one possibility - nonaj and klop so there is only one probability
of the user ID sets.


Example Input 2
 3
 poppolfgopjduhqertol
Output
6
Explanation
Since supervisor knows there are only 3 user IDs and they cannot start or end with a
vowel, there are following possibilities -

poppol fgop jduhqertol
poppol fgopj duhqertol
poppol fgopjduh qertol 
poppolf gopjduh qertol
poppolf gopj duhqertol
poppolfgop jduh qertol
Here there are 6 possibilities.

'''

def is_consonant(char):
    if char not in 'aeiou':
        return True
    return False

def possibilities(remaining_ids,curr_string,curr_users):
    #print(remaining_ids,curr_string,curr_users)
    ans = 0
    if len(curr_string)==0 and remaining_ids==0:
        #print(curr_users)
        return 1
    if len(curr_string) < 4:
        return ans
    
    start = 0
    end = start + 3
    for i in range(end,len(curr_string)):
        curr_user_id = curr_string[start:i+1]
        if is_consonant(curr_string[start]) and is_consonant(curr_string[i]) and curr_user_id not in curr_users:
            curr_users.add(curr_user_id)
            ans = ans + possibilities(remaining_ids-1,curr_string[i+1:],curr_users)
            curr_users.remove(curr_user_id)
    return ans


num_of_ids = int(input())
id_string = input()
curr_users = set()
ans=possibilities(num_of_ids,id_string,curr_users)
print(ans)









'''  #works for some cases only
def find(n,string,bidxes):
    #print(bidxes)
    count=0
    if n==4:
        for i in bidxes:
            f,s=int(i[0]),int(i[1])
            for j in bidxes:
                if i!=j:
                    t,ff=int(j[0]),int(j[1])
                    for k in bidxes:
                        if k!=j and k!=i:
                            fi,si=int(k[0]),int(k[1])
                            s1,s2,s3,s4=string[:f+1],string[s:t+1],string[ff:fi+1],string[si:]
                            if len(s1)>=4 and len(s2)>=4 and len(s3)>=4 and len(s4)>=4:
                                if string[0] not in vowels and string[-1] not in vowels:
                                    count+=1
    if n==3:
        for i in bidxes:
            f,s=int(i[0]),int(i[1])
            for j in bidxes:
                if i!=j:
                    t,ff=int(j[0]),int(j[1])
                    s1,s2,s3=string[:f+1],string[s:t+1],string[ff:]
                    if len(s1)>=4 and len(s2)>=4 and len(s3)>=4:
                        if string[0] not in vowels and string[-1] not in vowels:
                            count+=1
        
    if n==2:
        lis=bidxes[0]
        s1,s2= string[:int(lis[0])+1],string[int(lis[1]):]
        if len(s1)>=4 and len(s2)>=4:
                    if string[0] not in vowels and string[-1] not in vowels:
                        count+=1
    
    print(count)

n=int(input())
string=input()
#string='poppolfgopjduhqertol'
for i in string:
    if i.isdigit():
        print(0)
        exit(0)
vowels='aeiou'
bidxes=[]
for i in range(3,len(string)-4):
        s=string[i]+string[i+1]
        if s[0] not in vowels and s[1] not in vowels :
            l=[]
            l.append(i)
            l.append(i+1)
            bidxes.append(l)
#print(bidxes)
find(n,string,bidxes)
'''
