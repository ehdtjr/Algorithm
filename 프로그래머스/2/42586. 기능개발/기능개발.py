import sys
from collections import deque

def solution(progresses, speeds):
    answer = []
    que = deque(progresses)
    speeds=deque(speeds)
    cnt = 0
    while que:
        for i in range(len(que)):
            que[i] += speeds[i]

        while que:
            if que[0]>=100:
                que.popleft()
                speeds.popleft()
                cnt += 1
            else:
                break

        if cnt > 0:
            answer.append(cnt)
            cnt = 0

    return answer