n = int(input())

arr=[]
for i in range(n):
    x,y=map(str,input().split())
    arr.append(x)

arr_cp=list(set(arr))
arr_cp.sort(reverse=True)
d={x:0 for x in arr_cp}

for i in arr:
    d[i]+=1

for i in d.items():
    if i[1]%2!=0:
        print(i[0])