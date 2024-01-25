str=list(input())

N=int(input())
count=len(str)-1

arr=[]

for i in range(N):
    x=list(input())
    if x[0]=='L'and str:
        arr.append(str.pop())
    elif x[0]=='D' and arr:
        str.append(arr.pop())
    elif x[0]=='B'and str:
        str.pop()
    elif len(x)==3:
        str.append(x[2])

arr.reverse()

print("".join(str+arr))