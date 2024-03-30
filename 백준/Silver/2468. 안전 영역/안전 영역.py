import sys
from collections import deque

n=int(sys.stdin.readline())

graph=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited=[[False]*n for _ in range(n)]
arr=[]

cnt=0
maxNum=1

x=[0,0,-1,1]
y=[-1,1,0,0]
def bfs(i,j):
    que=deque([(i,j)])
    visited[i][j]=0

    while que:
        a,b=que.popleft()

        for i in range(4):
            dx=a+x[i]
            dy=b+y[i]

            if dx < 0 or dy<0 or dx>=n or dy>=n:
                continue

            if graph[dx][dy]!=0 and visited[dx][dy]==False:
                visited[dx][dy]=True
                que.append((dx,dy))

for i in range(n):
    for j in range(n):
        if graph[i][j]>maxNum:
            maxNum=graph[i][j]

for k in range(maxNum):
    for i in range(n):
        for j in range(n):
            if graph[i][j]<=k:
                graph[i][j]=0

    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0 and visited[i][j] == False:
                cnt += 1
                bfs(i, j)
    arr.append(cnt)
    visited = [[False] * n for _ in range(n)]
    cnt=0

print(max(arr))