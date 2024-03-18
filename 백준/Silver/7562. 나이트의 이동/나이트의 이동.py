import sys
from collections import deque

T=int(sys.stdin.readline().rstrip())

x=[-2,-2,-1,-1,1,1,2,2]
y=[-1,1,-2,2,-2,2,-1,1]

def dfs(l,x1,y1,x2,y2):
    que=deque([(x1,y1)])

    while que:
        a,b=que.popleft()

        if a==x2 and b==y2:
            return graph[a][b]

        else:
            for i in range(8):
                dx=a+x[i]
                dy=b+y[i]

                if dx<0 or dx>=l or dy<0 or dy>=l:
                    continue

                if graph[dx][dy]==0:
                    graph[dx][dy]=graph[a][b]+1
                    que.append((dx,dy))

for _ in range(T):
    i=int(sys.stdin.readline().rstrip())

    graph=[([0]*i)for _ in range(i)]

    x1,y1=map(int,sys.stdin.readline().split())
    x2,y2=map(int,sys.stdin.readline().split())

    print(dfs(i,x1,y1,x2,y2))
