import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

x = [0, 0, -1, 1]
y = [-1, 1, 0, 0]

def bfs(arr):
    length = len(arr)
    que = deque()

    for i in range(length):
        que.append(arr[i])

    while que:
        a, b = que.popleft()

        for i in range(4):
             dx = a + x[i]
             dy = b + y[i]

             if dx < 0 or dy < 0 or dx >= n or dy >= m:
                 continue

             if graph[dx][dy] == 0:
                 graph[dx][dy] = graph[a][b] + 1
                 que.append((dx, dy))

    for i in range(n):
        if 0 in graph[i]:
           return False

arr = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            arr.append((i, j))

result=bfs(arr)

count=0

if result == False:
  print(-1)
else:
    for i in range(n):
        if max(graph[i])>count:
            count=max(graph[i])
    print(count-1)