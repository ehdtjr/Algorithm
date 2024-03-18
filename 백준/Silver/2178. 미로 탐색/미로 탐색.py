import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())

miro=[list(map(int,sys.stdin.readline().rstrip()))for _ in range(n)]

dx=[0,0,1,-1]
dy=[-1,1,0,0]

def bfs(x,y):
    que=deque([(x,y)])

    while que:
        a,b=que.popleft()

        if a==(n-1) and b==(m-1):
            return miro[a][b]

        for i in range(4):
            px=a+dx[i]
            py=b+dy[i]

            if px<0 or px>=n or py<0 or py>=m:
                continue

            if miro[px][py]==1:
                miro[px][py]=miro[a][b]+1
                que.append((px,py))


print(bfs(0,0))