def solution(arr):
    answer = []
    for idx in range(len(arr)-1):
        if arr[idx]!=arr[idx+1]:
            answer.append(arr[idx])
    if arr:
        answer.append(arr[-1])
    return answer