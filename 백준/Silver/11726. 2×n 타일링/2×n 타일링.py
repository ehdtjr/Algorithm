import sys

n=int(sys.stdin.readline().rstrip())

arr=[0]*1001

for i in range(1,n+1):
    if i<=3:
        arr[i]=i
    else:
        arr[i]=arr[i-1]+arr[i-2]

print(arr[n]%10007)