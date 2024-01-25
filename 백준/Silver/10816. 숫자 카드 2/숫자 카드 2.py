N = int(input())
arr1=list(map(int,input().split()))
M = int(input())
arr2=list(map(int,input().split()))

d={x:0 for x in arr2}

for i in arr1:
    if i in d.keys():
        d[i]+=1

for i in arr2:
    if i in d:
        print(d[i],end=' ')
    else:
        print(0)