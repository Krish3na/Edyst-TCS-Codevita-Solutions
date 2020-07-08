'''
[CodeVita 2019] Digit Pairs
Given N three-digit numbers, your task is to find bit score of all N numbers and then print the number of pairs possible based on these calculated bit score.

Rule for calculating bit score from three digit number

From the 3-digit number:

extract largest digit and multiply by 11 then
extract smallest digit multiply by 7 then
add both the result for getting bit pairs.
Note: Bit score should be of 2-digits, if above results in a 3-digit bit score, simply ignore most significant digit.

Consider following examples:

Say, number is 286

Largest digit is 8 and smallest digit is 2
So, 8*11+2*7 =102 so ignore most significant bit , So bit score = 02.
Say, Number is 123

Largest digit is 3 and smallest digit is 1
So, 3*11+7*1=40, so bit score is 40.
Rules for making pairs from above calculated bit scores

Condition for making pairs are

Both bit scores should be in either odd position or even position to be eligible to form a pair.
Pairs can be only made if most significant digit are same and at most two pair can be made for a given significant digit.
Constraints
N<=500

Input Format

First line contains T the number of test cases. For each test case you have:
1 line contains an integer N, denoting the count of numbers
Next line contains N 3-digit integers delimited by space
Output

One integer value denoting the number of bit pairs.
Example Input
3
8 
234 567 321 345 123 110 767 111
7 
279 420 427 437 566 572 921
12 
154 252 320 586 590 613 743 814 824 868 902 936
Output
3
2
3
Explanation
First case
After getting the most and least significant digits of the numbers and applying the formula given in Rule 1 we get the bit scores of the numbers as:

58 12 40 76 40 11 19 18

No. of pair possible are 3:

40 appears twice at odd-indices 3 and 5 respectively. Hence, this is one pair.
12, 11, 18 are at even-indices. Hence, two pairs are possible from these three-bit scores.
Hence total pairs possible is 3

Second case
We get the bitscores as: 13 44 91 98 01 91 06

We can get the following pairs: 98 and 91, because they are at 4th and 6th position respectively

We can also get 01 and 06

Hence 2 pairs completely

Third Case
We get the bitscores as 62 69 33 23 99 73 98 95 02 30 99 20. In this we can form the following pairs:

23, 20, and 2 pairs from 99, 98, 99
'''

def pairs_from(i):
    if i==2:
        return 1
    elif i>=3:
        return 2
    return 0

t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    bitscore=[]
    for i in l:
        indi=list(str(i))
        summ=str(int(max(indi))*11+int(min(indi))*7)
        summ=str(summ)[-2:]
        bitscore.append(summ)
    #print(bitscore)
    even_pos_count=[0]*10
    odd_pos_count=[0]*10
    for i in range(len(bitscore)):
        index=int(bitscore[i][0])
        if (i+1)%2==0:
            even_pos_count[index]+=1
        else:
            odd_pos_count[index]+=1
    count_pairs=[0]*10
    for i in range(10):
        if even_pos_count[i]<=1 and odd_pos_count[i]<=1:
            continue
        count_pairs[i]+=pairs_from(even_pos_count[i])+pairs_from(odd_pos_count[i])
        count_pairs[i]=min(2,count_pairs[i])
    print(sum(count_pairs))
