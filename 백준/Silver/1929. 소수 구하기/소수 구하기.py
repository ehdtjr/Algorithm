M, N=map(int,input().split())

array=[0,0]
count=0

for i in range(2,N+1):
    array.append(i)

for i in range(2,N+1):
    if array[i]!=0:
        for j in range(i*i,N+1,i):
            array[j]=0

for i in range(M,N+1):
    if array[i]!=0:
        print(array[i])