import sys
from collections import deque

m,n,h=map(int,sys.stdin.readline().split())

graph=[[]for _ in range(h)]

x=[0,0,0,0,-1,1]
y=[0,0,-1,1,0,0]
z=[-1,1,0,0,0,0]

def bfs(arr):
    que=deque()

    for i in arr:
        que.append(i)

    while que:
        a,b,c=que.popleft()

        for i in range(6):
            dz=a+z[i]
            dx=b+x[i]
            dy=c+y[i]


            if dx<0 or dy<0 or dz<0 or dx>=n or dy>=m or dz>=h:
                continue

            if graph[dz][dx][dy]==0:
                graph[dz][dx][dy]=graph[a][b][c]+1
                que.append((dz,dx,dy))

    for i in range(h):
        for j in range(n):
            if 0 in graph[i][j]:
                return False


for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int,sys.stdin.readline().split())))

arr=[]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k]==1:
                arr.append((i,j,k))

result=bfs(arr)

cnt=0

if result==False:
    print(-1)
else:
    for i in range(h):
        for j in range(n):
            if max(graph[i][j])>cnt:
                cnt=max(graph[i][j])
    print(cnt-1)