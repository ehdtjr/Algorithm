import sys

v,e=map(int,sys.stdin.readline().split())

parent=[i for i in range(v+1)]
tree=[]
sum=0
cnt=0

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
        parent[a]=b
    else:
        parent[b]=a

for i in range(e):
    a,b,c=map(int,sys.stdin.readline().split())
    tree.append([c,a,b])

tree.sort()

for c,a,b in tree:
    if cnt==v-1:
        break

    if find(a)==find(b):
        continue
    else:
        union(a,b)
        sum+=c
        cnt+=1

print(sum)