import sys

n = int(sys.stdin.readline())

stack=[]

def push(arr):
    stack.append(arr[1])

def pop_1():
    if len(stack)!=0:
        print(stack.pop())
    else:
        print(-1)

def count():
    print(len(stack))

def check():
    if len(stack)==0:
        print(1)
    else:
        print(0)

def pop_2():
    if len(stack)!=0:
        print(stack[-1])
    else:
        print(-1)


for i in range(n):
    arr=list(map(int,sys.stdin.readline().split()))
    if arr[0]==1:
        push(arr)
    elif arr[0]==2:
        pop_1()
    elif arr[0]==3:
        count()
    elif arr[0]==4:
        check()
    else:
        pop_2()