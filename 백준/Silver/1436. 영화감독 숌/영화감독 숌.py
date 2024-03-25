import sys

n= int(sys.stdin.readline())
arr=[0]

for i in range(666,10000000):
    if '666' in str(i):
        arr.append(i)

print(arr[n])