'''

CodeVita 2014, Expense Solver
Expense Solver
N number of friends share accommodation. Expenses between them are shared. They have a rule that expenses are shared equally among all friends those who are a party to that expense. Their problem is they are poor in math. Hence they end up fighting over expenses. Your job is to help them in splitting the expenses and prevent in-fighting.

Write a program to help divide the expenses. The program should be generic enough such that number of members sharing accommodation can vary. Your program should take the following inputs and give the following output.

Assumptions:

The Person paying for a transaction is himself a party in that particular expense

Input Format:
The first line contains N space separated strings, which are the names of the friends.
The second line contains k, the number of inputs. Following lines contain:

Line 1 contains the name of the friends sharing the accommodation, separated by white space character
Line 2 provides the number of transactions(T) to be accounted. Line 3 to line T+2 will give the details of the transactions and will contain the spender’s name, the amount spent and the friends involved in the transactions
Ns1 A Np1 Np2...
where Ns is the spender, A is the amount spent in a particular transaction and Npi are the other friends involved in the transaction
Output Format:
For Valid Input, print

N1 A1
N2 -A2
...
Nn -An
where Ni is the name of the friend and Ai is the amount he has to receive/pay. Negative(-) number represents payable.

Sample Input / Output
Input:

Pankaj Pranav Mayank Nihit Mukesh
5
Pankaj 600 Pranav Mayank
Pranav 450 Mayank Nihit
Mayank 300 Mukesh Pranav Nihit
Nihit 1200 Pranav Pankaj
Mukesh 3000 Pranav Pankaj Mayank
Output:

Pankaj -750.0
Pranav -1125.0
Mayank -875.0
Nihit 575.0
Mukesh 2175.0
Input:

Sagar Sumit Suresh
4
Sagar Sumit
Output:

Invalid Input

'''

if __name__ == "__main__":
    try:
        friends = input().strip().split()
        assert len(friends) > 0

        passbook = dict([(f, 0) for f in friends])
        T = int(input())
        assert 0 < T < 100000

        for _ in range(T):
            payer, total, *payees = input().strip().split()
            payees.append(payer)
    
            assert payer in friends
            for p in payees:
                assert p in friends

            total = float(total)
            assert total >= 0.0
            
            per_person = total / len(payees)

            for p in payees:
                passbook[p] -= per_person

            passbook[payer] += total

        for f in friends:
            print(f"{f} {passbook[f]:.2f}")

    except:
        print("Invalid Input")
