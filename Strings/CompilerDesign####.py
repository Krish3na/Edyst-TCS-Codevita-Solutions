'''

Codevita [2014] Compiler Design
Compiler Design - Limit the Method Instructions
Raj is a newbie to the programming and while learning the programming language he came to know the following rules:

Each program must start with { and end with }.
Each program must contain only one main function. Main function must start with < and end with >.
A program may or may not contain user defined function(s). There is no limitation on the number of user defined functions in the program. User defined function must start with ( and end with ).
Loops are allowed only inside the functions (this function can be either main function or user defined function(s)). Every loop must start with { and end with }.
User defined function(s) are not allowed to be defined inside main function or other user defined function(s).
Nested loops are allowed.
Instructions can be anywhere inside the program.
Number of instructions inside any user defined function must not be more than 100.
If any of the above conditions is not satisfied, then the program will generate compilation errors. Today Raj has written a few programs, but he is not sure about the correctness of the programs. Your task is to help him to find out whether his program will compile without any errors or not.

Input Format:
First line starts with T, number of test cases.
Each test case will contain a single line L, where L is a program written by Raj.

Output Format:
Print No Compilation Errors if there are no compilation errors, else print Compilation Errors.

Constraints:
1<=T<=100

L is a text and can be composed of any of the characters {, }, (, ), <, >and P, where P will represents the instruction.

L, comprised of characters mentioned above should be single spaced delimited.
Number of characters in the text, |L| < = 10000

Sample Input and Output
Input

3
{ < > ( P ) }
{ < { } > ( { } ) )
{ ( { } ) }
Output

No Compilation Errors
Compilation Errors
Compilation Errors

'''

def check(s):
    flag = 0
    end = 0
    count = 0
    if s[0]!='{' or s[-1]!='}':
        print('Compilation Errors')
        return
    for i in range(1,len(s)):
        if s[i]=='<':
            if flag!=0:
                print('Compilation Errors')
                return
            for j in range (i+1,len(s)):
                if s[j]=='>':
                    end=j
                    break
            if end==0:
                print('Compilation Errors')
                return
            for k in range (i+1,end+1):
                if s[k]=='(':
                    print('Compilation Errors')
                    return
            flag += 1
            end=0
        if s[i]=='(':
            for j in range(i+1,len(s)):
                if s[j]==')':
                    end = j
                    break
            if end==0:
                print('Compilation Errors')
                return
            for k in range (i+1,end+1):
                if s[k]=='(':
                    print('Compilation Errors')
                    return
            end=0
        if s[i]!='>' and s[i]!='}' and s[i]!=')' and s[i]!=' ':
            count += 1
    
    
    if flag ==0 or count>100:
        print('Compilation Errors')
    else:
        print('No Compilation Errors')


t= int(input())
for i in range(t):
    s = input().strip()
    #s="{<{}{{()}}> ( { } ) }"
    #print(s)
    check(s)

'''
###Ignore this code
def isopen(a):
    return a=='<' or a=='{' or a=='('

def isclosed(a):
    return a=='>' or a=='}' or a==')'

def isequivalent(a,b):
    if a=='(' and b==')':
        return True
    if a=='<' and b=='>':
        return True
    if a=='{'and b=='}':
        return True
    return False

def checkforfunc(stack):
    idx=0
    lis=[]
    for i in stack:
        if i=='<':
            idx=stack.index(i)
            lis=stack[idx+1:]
    if '(' in lis:
        return True
    return False
        

t=int(input())
for i in range(t):
    string = input().strip().split()
    #{ < > ( P ) }
    stack=[]
    instruc=0
    mainf=0
    balanced = True
    for i  in range(len(string)):
        curr = string[i]
        #print('curr',curr)
        if isopen(curr):
            if curr=='<':
                if mainf <= 1:
                    mainf+=1
            stack.append(curr)
            
        if curr=='P':
            if instruc < 100:
                instruc += 1
            else:
                balanced = False
                break
            
        if isclosed(curr):
            if len(stack)==0:
                balanced = False
            
            else:
                if curr=='>' or curr==')':
                    if checkforfunc(stack):
                        balanced = False
                        break
                popped = stack.pop()
                #print(popped)
            
                while not isopen(popped) and len(stack)!=0:
                    popped = stack.pop()
                
                if  isopen(popped):
                    #print(9)
                    if isequivalent(popped,curr):
                        #print(9)
                        balanced = True
                    
                    else:
                        balanced = False
                        break
        if mainf >1 or mainf==0:
            balanced = False
                    
    if balanced==True:
        print('No Compilation Errors')
    else:
        print('Compilation Errors')

'''          
