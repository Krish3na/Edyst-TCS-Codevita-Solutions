'''
CodeVita 2016, Christmas Tree
Christmas Tree
Chirag is a pure Desi boy. And his one and only dream is to meet Santa Claus. He decided to decorate a Christmas tree for Santa on coming Christmas. Chirag made an interesting Christmas tree that grows day by day.

The Christmas tree is comprised of the following

Parts
Stand
Each Part is further comprised of Branches. Branches are comprised of Leaves.

How the tree appears as a function of days should be understood. Basis that print the tree as it appears on the given day. Below are the rules that govern how the tree appears on a given day.

Write a program to generate such a Christmas tree whose input is number of days.

Rules:

If tree is one day old you cannot grow. Print a message “You cannot generate christmas tree”
Tree will die after 20 days; it should give a message “Tree is no more”
Tree will have one part less than the number of days. E.g.
On 2nd day tree will have 1 part and one stand.
On 3rd day tree will have 2 parts and one stand
On 4th day tree will have 3 parts and one stand and so on.
Top-most part will be the widest and bottom-most part will be the narrowest.
Difference in number of branches between top-most and second from top will be 2
Difference in number of branches between second from top and bottom-most part will be 1
Below is an illustration of how the tree looks like on 4th day

4th Day Illustration

Input Format:
First line of input contains k - the number of inputs
The next k lines denote the number of days N

Output Format:
Print Christmas Tree for given N

OR

Print “You cannot generate christmas tree” if N <= 1

OR

Print “Tree is no more” if N > 20

Constraints:
0<= N <=20
Example:
Input:
k = 2
 
N = 1
 
N = 2
Output:
You cannot generate christmas tree
  *
 ***
*****
  *  
  *

'''

k = int(input())
 
for i in range(1,k+1):
    n = int(input())
    if(n<=1):
        print("You cannot generate christmas tree")
    elif(n>20):
        print("Tree is no more")
    elif(n>1 and n<=20):
        for p in range(1,n):
            if(p==1):
                print(" "*n,end="")
                print("*")
            for r in range(2,n+3-p):
                print(" "*(n-r+1),end="")
                print("*"*(2*r-1))
        print(" "*n,end="")
        print("*")
        print(" "*n,end="")
        print("*")


