import sys
sys.setrecursionlimit(10**6)

n,m=map(int,sys.stdin.readline().split())

graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for i in range(m):
    u,v=map(int,sys.stdin.readline().split())

    graph[u].append(v)
    graph[v].append(u)

cnt=0

def dfs(i):
    visited[i]=True

    for j in graph[i]:
        if visited[j]==False:
            visited[j]=True
            dfs(j)

for i in range(1,n+1):
    if visited[i]==False:
        cnt+=1
        dfs(i)

print(cnt)