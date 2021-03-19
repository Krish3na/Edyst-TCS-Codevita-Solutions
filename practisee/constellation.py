N=int(input())
first=list(input().split())
second=list(input().split())
third=list(input().split())
col=0
#print(first)
#print(second)
#print(third)
while (col<N-2):
    #print(col)
    if (first[col]=='#' and second[col]=='#' and third[col]=='#'):
        print('#',end='')
        col = col + 1
        continue #used to skip rest of code to reduce running time of program
          
    elif (first[col]=='.' and second[col]=='.' and third[col]=='.'):
        col = col + 1
        continue
          
    elif first[col]=='*' and first[col+1]=='.' and first[col+2]=='*':
        if second[col]=='*' and second[col+1]=='.' and second[col+2]=='*':
            if third[col]=='*' and third[col+1]=='*' and third[col+2]=='*' :
                print('U',end='')
                col = col + 3
                continue
        
    
    elif first[col]=='.' and first[col+1]=='*' and first[col+2]=='.':
        if second[col]=='*' and second[col+1]=='*' and second[col+2]=='*':
            if third[col]=='*' and third[col+1]=='.' and third[col+2]=='*' :
                print('A',end='')
                col = col + 3
                continue
        
    elif first[col]=='*' and first[col+1]=='*' and first[col+2]=='*':
        if second[col]=='.' and second[col+1]=='*' and second[col+2]=='.':
            if third[col]=='*' and third[col+1]=='*' and third[col+2]=='*' :
                print('I',end='')
                col = col + 3
                continue
        elif second[col]=='*' and second[col+1]=='.' and second[col+2]=='*':
            if third[col]=='*' and third[col+1]=='*' and third[col+2]=='*' :
                print('O',end='')
                col = col + 3
                continue
        elif second[col]=='*' and second[col+1]=='*' and second[col+2]=='*':
            if third[col]=='*' and third[col+1]=='*' and third[col+2]=='*' :
                print('E',end='')
                col = col + 3
                continue


    else:
        col = col + 1
        continue
