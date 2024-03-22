import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
graph=[list(map(int,sys.stdin.readline().rstrip()))for _ in range(n)]

visited[0][0][0]=1

x=[0,0,-1,1]
y=[-1,1,0,0]

def bfs():
    que=deque([(0,0,0)])

    while que:
        a,b,c=que.popleft()
        
        if a==n-1 and b==m-1:
            return visited[a][b][c]

        for i in range(4):
            dx=a+x[i]
            dy=b+y[i]

            if dx < 0 or dy< 0 or dx>=n or dy>=m :
                continue

            if graph[dx][dy]==0 and visited[dx][dy][c]==0:
                visited[dx][dy][c]=visited[a][b][c]+1
                que.append((dx,dy,c))

            elif graph[dx][dy]==1 and c==0:
                visited[dx][dy][1]=visited[a][b][0]+1
                que.append((dx,dy,1))
    return -1
                
print(bfs())