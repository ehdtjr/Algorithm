import sys
from collections import deque

n=int(sys.stdin.readline())

grid=[]
visited=[[False] *(n) for _ in range(n)]

for i in range(n):
    grid.append(list(map(str,sys.stdin.readline().rstrip())))

cnt=[0,0]

x=[0,0,-1,1]
y=[-1,1,0,0]
def bfs(i,j):
    que=deque([(i,j)])
    visited[i][j]=True

    while que:
        a,b=que.popleft()

        for k in range(4):
            dx=a+x[k]
            dy=b+y[k]

            if dx < 0 or dy< 0 or dx>=n or dy>=n:
                continue

            if grid[dx][dy] == grid[a][b] and visited[dx][dy]==False:
                que.append((dx,dy))
                visited[dx][dy]=True


for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            cnt[0]+=1
            bfs(i,j)

visited=[[False] *(n) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j]=='G':
            grid[i][j]='R'

for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            cnt[1]+=1
            bfs(i,j)

print(*cnt)

