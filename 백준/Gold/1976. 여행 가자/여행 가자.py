import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph=[[]for _ in range(n+1)]

parent=[i for i in range(n+1)]
def find(i):
    if parent[i]==i:
        return i
    else:
        parent[i]=find(parent[i])
        return parent[i]

def union(i,j):
    i=find(i)
    j=find(j)

    if i>j:
        parent[i]=j
    else:
        parent[j]=i

def check(parent,plan):
    a=parent[plan[0]]
    for i in plan:
        if parent[i]==a:
            continue
        else:
            print('NO')
            return
    print('YES')
    return

for i in range(n):
    arr=list(map(int,sys.stdin.readline().split()))
    for j in range(len(arr)):
        if arr[j]==1:
            if find(i+1)==find(j+1):
                continue
            else:
                union(i+1,j+1)

plan=list(map(int,sys.stdin.readline().split()))

check(parent,plan)