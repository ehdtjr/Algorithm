import sys
# sys.setrecursionlimit(10**8)

N , M=map(int,sys.stdin.readline().split())

graph=[[]for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if i>=j :
            continue
        else:
            graph[i].append(j)

arr=[]

def dfs (i):
    arr.append(i)

    if len(arr)==M :
        print(*arr)
        return

    for j in graph[i]:
        if j not in arr:
            dfs(j)
            arr.pop()
        else:
            continue


for i in range(1,N+1):
    arr.clear()
    dfs(i)
