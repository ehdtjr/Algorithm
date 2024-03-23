import sys
from collections import deque

k = int(sys.stdin.readline().rstrip())

def bfs(graph,visited):
    for i in range(1,len(visited)):
        if visited[i]!=0:
            continue
        visited[i]=1

        que=deque([i])
    
        while que:
            x=que.popleft()

            next_val=visited[x]%2+1

            for i in graph[x]:
                if visited[i]==0:
                    visited[i]=next_val
                    que.append(i)
                elif visited[i]!=next_val:
                    return False

    return True

for _ in range(k):
    v,e=map(int,sys.stdin.readline().split())

    graph=[[] for _ in range(v+1)]
    visited=[0]*(v+1)

    for i in range(e):
        x,y=map(int,sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)

    result=bfs(graph,visited)

    if result==False:
        print("NO")
    else:
        print("YES")