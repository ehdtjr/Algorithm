import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

miro = []

for i in range(N):
    miro.append(list(map(int, sys.stdin.readline().rstrip())))

cnt = 0
max = N * M

x = [0, 0, 1, -1]
y = [-1, 1, 0, 0]


def bfs(i, j):
    que = deque([(i, j)])

    while que:
        a, b = que.popleft()

        for k in range(4):
            dx = a + x[k]
            dy = b + y[k]

            if dx < 0 or dx >= N or dy < 0 or dy >= M:
                continue

            if miro[dx][dy] == 1:
                miro[dx][dy]=miro[a][b]+1
                que.append((dx, dy))
                
    return miro[N-1][M-1]

print(bfs(0, 0))
