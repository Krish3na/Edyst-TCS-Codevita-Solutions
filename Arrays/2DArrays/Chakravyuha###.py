def printC(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end='\t')
        print()
        
N = int(input())
arr=[[0 for i in range(N)] for j in range(N)]

power_points = 1 + N*N//11
pp_idxes=[[0,0]]

end_row,end_col=0,0
counter=1

if N ==1:  #edge case
    arr[0][0]=counter
    
for i in range(N//2): #printing N//2 squares
    row = i
    col = i
    
    end_col=N-i-1   #printing top row of square
    while(col<end_col):
        arr[row][col]=counter
        if counter%11==0:
            l=[row,col]
            pp_idxes.append(l)
        col+=1
        counter+=1
        
    end_row=N-i-1   #printing right column of square
    while(row<end_row):
        arr[row][col]=counter
        if counter%11==0:
            l=[row,col]
            pp_idxes.append(l)
        row+=1
        counter+=1

    end_col=i      #printing bottom row of square
    while(col>end_col):
        arr[row][col]=counter
        if counter%11==0:
            l=[row,col]
            pp_idxes.append(l)
        col-=1
        counter+=1

    end_row=i    #printing left column of square
    while(row>end_row):
        arr[row][col]=counter
        if counter%11==0:
            l=[row,col]
            pp_idxes.append(l)
        row-=1
        counter+=1
        
    if N%2==1:  #if odd we are left with a element, add it seperately
        arr[N//2][N//2]=N*N
        if N*N%11==0:
            l=[N//2,N//2]
            pp_idxes.append(l)
        
    

#printC(arr)   

print('Total Power points :',power_points)
for pp in pp_idxes:
    print('(',pp[0],',',pp[1],')',sep='')

