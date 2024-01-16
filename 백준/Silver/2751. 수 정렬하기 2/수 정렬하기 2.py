N = int(input())

arr=[]

for i in range(N):
    x=int(input())
    arr.append(x)

arr.sort()
for i in arr:
    print(i)