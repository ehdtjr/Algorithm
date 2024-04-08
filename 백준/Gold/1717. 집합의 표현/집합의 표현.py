import sys
sys.setrecursionlimit(10**8)

v,e=map(int,sys.stdin.readline().split())

parent=[i for i in range(v+1)]

def find(i):
    if parent[i]==i:
        return parent[i]
    else:
        parent[i]=find(parent[i])
        return parent[i]

def union(a,b):
    a=find(a)
    b=find(b)

    if a>b:
        parent[b]=a
    else:
        parent[a]=b

for i in range(e):
    c,a,b=map(int,sys.stdin.readline().split())

    if c==0:
        union(a,b)
    else:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')
