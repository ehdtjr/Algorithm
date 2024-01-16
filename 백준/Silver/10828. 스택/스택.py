N = int(input())

arr=[]
result=[]
def push(num):
    arr.append(int(num))

def pop():
    i=len(arr)
    if i==0:
        result.append(-1)
    else:
        result.append(arr[i-1])
        arr.pop()

def size():
    result.append(len(arr))

def empty():
    if len(arr)==0:
        result.append(1)
    else:
        result.append(0)

def top():
    if len(arr)==0:
        result.append(-1)
    else:
        result.append(arr[-1])

for i in range(N):
    x=list(map(str,input().split()))
    if len(x)==2:
        push(int(x[1]))
    elif x[0]=='pop':
        pop()
    elif x[0]=='size':
        size()
    elif x[0]=='empty':
        empty()
    else:
        top()
for i in result:
    print(i)