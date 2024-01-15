N = int(input())

arr=[]
N=str(N)

for i in range(len(N)):
    arr.append(N[i])

arr.sort(reverse=True)
for i in arr:
    print(i,end='')