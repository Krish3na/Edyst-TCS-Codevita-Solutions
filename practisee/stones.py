'''
Mars Stone
Rob has gone to Mars to collect some stones. The bag he is carrying can hold a maximum weight of M.
There are M stones weighing from 1 to Min Mars. There are N stones on Mars that are similar to the
ones on Earth. Find the number of stones he can bring from Mars such that none of them are similar to
any stone on Earth.

Input Specification:
input1: M. denoting the size of the bag and the number of different stone
weights present on Mars.
input2: N, denoting the number of common stones on Earth and Mars.
input3: An N element array containing the list of the weights of the common
stones,

Output Specification:
Your function should return the maximum unique stones that can be collected
from Mars.​
 '''

def calculate(M,N,n):
    i_sum=M
    maxx=-100000
    l=n[:]
    

    for i in range(1,M+1):
        count=0
        if i not in l:
            summ=i_sum-i
            #print('i',summ)
            
            for j in range(i+1,M+1):
                if j not in l and summ-j>=0:
                    summ=summ-j
                    #print('j',summ)
                    count+=1
                    #print(count)
            maxx=max(count,maxx)

    return maxx

M=12
N=4
n=[1,5,7,9]

print(calculate(M,N,n))

from datetime import datetime
print(datetime(1970,1,1).strftime('%Y-%d-%B'))
print([n for n in range(10) if n % 2])
def my_func(n1, n2): return n1 + n2
my_func(1, 2, 3)
