import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph=[]
parent=[i for i in range(n+1)]
cnt=0

def find(x):
    if x==parent[x]:
        return x
    else:
        parent[x]=find(parent[x])
        return parent[x]

def union(a,b):
    x=find(a)
    y=find(b)

    if x<y:
        parent[y]=x
    else:
        parent[x]=y

for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph.append([c,a,b])

graph.sort()

for c,a,b in graph:
    if find(a)!=find(b):
        union(a,b)
        cnt+=c

print(cnt)