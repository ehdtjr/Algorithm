from collections import deque

def solution(progresses, speeds):
    answer = []
    cnt=0
    
    dq_p=deque(progresses)
    dq_s=deque(speeds)
    
    while len(dq_p)!=0:
        for i in range(len(dq_p)):
            dq_p[i]+=dq_s[i]

        while dq_p[0]>=100:
            dq_p.popleft()
            dq_s.popleft()
            cnt+=1
            
            if len(dq_p)==0:
                break
            
        if cnt!=0:
            answer.append(cnt)
            cnt=0
    
    return answer