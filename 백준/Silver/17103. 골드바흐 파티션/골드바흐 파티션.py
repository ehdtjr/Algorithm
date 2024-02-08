from itertools import combinations_with_replacement

T=int(input())

arr=[True for _ in range(1000001)]

for i in range(2,1001):
    if arr[i]:
       for j in range(i+i,1000001,i):
           arr[j]=False

for i in range(T):
    count=0
    N=int(input())

    for i in range(2,N//2+1):
        if arr[i] and arr[N-i]:
            count+=1
    print(count)