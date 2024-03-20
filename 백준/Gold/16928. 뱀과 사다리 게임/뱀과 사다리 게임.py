import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())

pan=[0]*101
visit=[0]*101

num=1

def bfs(pan):
    que=deque([1])

    while que:
        x=que.popleft()

        if visit[100]!=0:
            return

        for i in range(1,7):
            if x+i>=101:
                continue

            if pan[x+i]!=0:
                if visit[pan[x+i]] == 0:
                    visit[pan[x+i]] = visit[x] + 1
                    que.append(pan[x+i])

            elif pan[x+i]==0:
                if visit[x+i]==0:
                    visit[x+i]=visit[x]+1
                    que.append(x+i)

for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    pan[x]=y

for i in range(m):
    u,v=map(int,sys.stdin.readline().split())
    pan[u]=v

bfs(pan)

print(visit[100])