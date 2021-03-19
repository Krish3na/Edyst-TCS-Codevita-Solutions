'''

Codevita [2014] Employee Hierarchy
Employee Hierarchy
Adam is working in a large hierarchical organization, where every employee, except the CEO, is either a supervisor or a sub-ordinate or both. Every employee will be identified by Employee ID. CEO of the company has 1 as his employee id. Every employee will get the salary (S) in accordance with their level and their performance. Given the data about the all the above mentioned details, your task is to find out the number of sub-ordinates with salary less than Adam.

If an employee appears at two different levels, then consider the level which is near (best) to the CEO.
An employee is considered as sub-ordinate, if Adam is a direct or indirect supervisor to the said employee.
Input Format
Input consists of three parts, viz.

First line contains T, the number of test cases. The following lines contain:
First Line contains, number of employees (N), number of supervisor-subordinate relationships (M) and Adam’s employee id (A)
Next M lines follow, each line contains two employee Ids I, J which represents that I is a supervisor of J.
Salaries of N employees, delimited by space
Output Format
Print the total number of employees who are sub-ordinates to Adam and have salary less than Adam’s.

Constraints:
1<=N<=50
1<=M<=1000
1<=I, J<=N
1<=S<=50000
Sample Input and Output
Input

5 5 2
1 2
2 3
2 4
4 5
5 3
1500 2000 1500 2500 1800
Output

2
'''
import queue


def solve(N, M, A, relationships, salaries):
    assert M == len(relationships)
    assert N == len(salaries)

    # supervision graph {id: set(of subordinate ids)}
    subs = {}
    for i in range(N):
        subs[i] = set()
    for i, j in relationships:
        subs[i].add(j)

    # add adam's immediate subordinates to a queue
    sq = queue.Queue()
    for i in subs[A]:
        sq.put(i)

    # for each sub s in the queue, add s and the subordinates of s to adam's
    #   list of subordinates as well
    adamsubs = set()
    while not sq.empty():
        S = sq.get()
        adamsubs.add(S)
        for i in subs.get(S, set()):
            if i not in adamsubs:
                sq.put(i)

    # count the number of subordinates (direct or indirect) of adam who earn lesser than he does
    print(len([s for s in adamsubs if salaries[s] < salaries[A]]))


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, M, A = map(int, input().strip().split())
        A = A - 1

        relationships = []
        for _ in range(M):
            i, j = map(int, input().strip().split())
            relationships.append((i - 1, j - 1))

        salaries = list(map(int, input().strip().split()))

        solve(N, M, A, relationships, salaries)
