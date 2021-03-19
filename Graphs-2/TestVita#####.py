'''
Testvita
TCS is working on a new project called "TestVita". There are N modules in the project. Each module i has completion time denoted in number of hours H(i) and may depend on other modules. If Module x depends on Module y then one needs to complete y before x.

As Project manager, you are asked to deliver the project as early as possible.
Provide an estimation of amount of time required to complete the project.

Input Format:

First line contains T, number of test cases.

For each test case:

First line contains N, number of modules.
Next N lines, each contain:
(i) Module ID
(Hi) Number of hours it takes to complete the module
(D) Set of module ids that i depends on - integers delimited by space.
Output Format:

Output the minimum number of hours required to deliver the project.

Constraints:
1 <= T <= 10
0 < N < 1000; number of modules
0 < i <= N; module ID
0 < Hi < 60; number of hours it takes to complete the module i
0 <= |D| < N; number of dependencies
0 < Dk <= N; module ID of dependencies
Sample Input and Output

Input:
1
5
1 5 0
2 6 1
3 3 2
4 2 3
5 1 3

Output:
16
'''

T = int(input())

for case in range(T):
    N = int(input())
    time_taken = 0
    hours = [0] * (N+1)
    indegrees = [0] * (N+1)
    timeline = [0] * (N+1)
    edges = []
    
    for e in range(N+1):
        edges.append([])

    
    for m in range(N):
        inp = input()
        inp = list(map(int,inp.split()))
        module_id = inp[0]
        hours[module_id] = inp[1]
        for dependency in inp[2:]:
            if(dependency>0):
                edges[dependency].append(module_id)
                indegrees[module_id]+= 1
        #print(edges)
    q = []
    for vertex in range(1,N+1):
        if(indegrees[vertex]==0):
            q.append(vertex)
    
    while(len(q)>0):
        curr_vertex = q.pop(0)
        timeline[curr_vertex] = hours[curr_vertex] + timeline[curr_vertex]
        time_taken = max(time_taken, timeline[curr_vertex])
        for neighbour in edges[curr_vertex]:
            indegrees[neighbour] = indegrees[neighbour]-1
            timeline[neighbour] = max(timeline[curr_vertex],timeline[neighbour])
            time_taken = max(time_taken, timeline[neighbour])
            if(indegrees[neighbour]==0):
                q.append(neighbour)
    print(time_taken)
