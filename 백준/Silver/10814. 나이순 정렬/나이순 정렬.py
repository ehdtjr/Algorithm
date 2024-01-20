n = int(input())

arr=[]

for i in range(n):
    x,y=map(str,input().split())
    arr.append([int(x),i,y])

arr.sort()

for i in range(n):
    print(arr[i][0],arr[i][2])