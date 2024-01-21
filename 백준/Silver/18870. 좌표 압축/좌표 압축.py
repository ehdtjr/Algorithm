n = int(input())

arr = list(map(int, input().split()))
arr_cp = list(set(arr.copy()))

arr_cp.sort()

d ={i : arr_cp[i] for i in range(len(arr_cp))}
d={v:k for k,v in d.items() }

for i in arr:
    print(d[i],end=' ')