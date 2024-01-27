N , M = map(int,input().split())

d = {}
arr=[]
result=[]

for i in range(N+M):
    arr.append(input())
    d[arr[i]]=0

for i in arr:
    d[i]+=1

for i in d.keys():
    if d[i]==2:
        result.append(i)

print(len(result))

result.sort()

for i in result:
    print(i)