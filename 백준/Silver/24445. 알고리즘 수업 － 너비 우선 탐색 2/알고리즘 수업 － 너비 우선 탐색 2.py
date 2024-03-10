import sys
from collections import deque


N, M, R=map(int,sys.stdin.readline().split())

graph=[[]for _ in range(N+1)]
visit=[0]*(N+1)

for _ in range(M):
  u,v=map(int,sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)

cnt=1

def bfs(r):
  global cnt
  visit[r]=cnt
  cnt+=1
  que=deque([r])

  while que:
    x=que.popleft()
    graph[x].sort(reverse=True)
    for i in graph[x]:
      if visit[i]==0:
        que.append(i)
        visit[i]=cnt
        cnt+=1

bfs(R)

for i in range(1,N+1):
  print(visit[i])

