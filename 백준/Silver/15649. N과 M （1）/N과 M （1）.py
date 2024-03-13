import sys

N,M=map(int,sys.stdin.readline().split())

graph=[[]for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            continue
        else:
            graph[i].append(j)

arr=[]
cnt=1
def dfs(i):
    global cnt
    arr.append(i)

    if cnt == M:
        print(*arr)
        return

    for j in graph[i]:
        if j not in arr:
            cnt+=1
            dfs(j)
            arr.pop()
            cnt -= 1
        else:
            continue

for i in range(1,N+1):
    if M==1:
        print(i)
    else:
        arr.clear()
        dfs(i)