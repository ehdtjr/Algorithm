T = int(input())

result=[]

for i in range(T):
    arr=list(input().split())
    for j in range(len(arr)):
        result.append(arr[j][-1::-1])
    print(*result)
    result=[]