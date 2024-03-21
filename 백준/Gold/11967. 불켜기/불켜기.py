import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())

graph=[[]for _ in range(n)]
light=[[0]*n for _ in range(n)]
visit=[[0]*n for _ in range(n)]

for i in range(n):
    for _ in range(n):
        graph[i].append([])

for i in range(m):
    a,b,c,d=map(int,sys.stdin.readline().split())
    a,b,c,d=a-1,b-1,c-1,d-1
    graph[a][b].append((c,d))

x=[0,0,-1,1]
y=[-1,1,0,0]

def bfs():
    light[0][0]=1
    visit[0][0]=1
    que=deque([(0,0)])

    while que:
        a,b=que.popleft()

        for i in range(len(graph[a][b])):
            q,w=graph[a][b][i]
            light[q][w]=1

        for i in range(4):
            dx=a+x[i]
            dy=b+y[i]

            if dx<0 or dy<0 or dx>=n or dy>=n:
                continue

            if visit[dx][dy]==0 and light[dx][dy]==1:
                visit[dx][dy]=1
                que.append((dx,dy))

                for i in range(len(graph[dx][dy])):
                    q,w=graph[dx][dy][i]

                    for j in range(4):
                        dq=q+x[j]
                        dw=w+y[j]

                        if dq < 0 or dw < 0 or dq >= n or dw >= n:
                            continue
                        if light[dq][dw]==1 and visit[dq][dw]==1:
                            que.append((dq,dw))

bfs()
cnt=0
for i in range(n):
    for j in range(n):
        if light[i][j]==1:
            cnt+=1

print(cnt)
