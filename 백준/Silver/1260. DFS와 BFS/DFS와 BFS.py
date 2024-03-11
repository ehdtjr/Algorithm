import sys
sys.setrecursionlimit(10**8)
from collections import deque

N,M,V=map(int,sys.stdin.readline().split())

graph=[[]for _ in range(N+1)]
visit_dfs=[False]*(N+1)
visit_bfs=[False]*(N+1)
arr_dfs=[]
arr_bfs=[]

for _ in range(M):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(r):
    visit_bfs[r]=True
    que=deque([r])

    while que:
        x=que.popleft()
        arr_bfs.append(x)
        graph[x].sort()
        for i in graph[x]:
            if visit_bfs[i]==False:
                visit_bfs[i]=True
                que.append(i)

def dfs(r):
    visit_dfs[r]=True
    arr_dfs.append(r)

    graph[r].sort()
    for i in graph[r]:
        if visit_dfs[i]==False:
            visit_dfs[i]=True
            dfs(i)

bfs(V)
dfs(V)

for i in range(len(arr_dfs)):
    print(arr_dfs[i],end=' ')

print()

for i in range(len(arr_bfs)):
    print(arr_bfs[i],end=' ')
