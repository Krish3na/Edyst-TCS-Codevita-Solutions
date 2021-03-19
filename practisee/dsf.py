def solve(one,two,k):
    idxMap=[0]*len(one)
    for i in range(k): 
        minn=100000000000
        oneIdx = -1
        twoIdx = -1
        

        for j in range(len(one)): 
            if (idxMap[j] == len(two)): 
                continue


            if (one[j] + two[idxMap[j]] < minn) :
                minn = one[j] + two[idxMap[j]]
                oneIdx = j
                twoIdx = idxMap[j]

        idxMap[oneIdx]+=1
        print (one[oneIdx]," ",two[twoIdx],end='')
        print (', ',end='')

one= [1, 7, 11]
two=[2, 4, 6]
k = 3
solve(one,two,k)
