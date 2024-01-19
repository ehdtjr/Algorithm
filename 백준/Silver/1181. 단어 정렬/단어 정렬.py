N = int(input())

arr=[]
word=[]

for i in range(N):
    x=input()
    length=len(x)

    if x not in word:
        word.append(x)
        arr.append([length,x])

arr.sort()

for i in range(len(arr)):
    print(arr[i][1])