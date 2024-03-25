import sys
sys.setrecursionlimit(1000000)

n=int(sys.stdin.readline())

graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
arr=[0]*(n+1)

cnt=2
def dfs(i):
    visited[i]=1

    global cnt

    for j in graph[i]:
        if arr[j]==0:
            arr[j]=i

        if visited[j]==0:
            dfs(j)


for i in range(1,n):
    v,u=map(int,sys.stdin.readline().split())
    graph[v].append(u)
    graph[u].append(v)

dfs(1)

for i in range(2,n+1):
    print(arr[i])