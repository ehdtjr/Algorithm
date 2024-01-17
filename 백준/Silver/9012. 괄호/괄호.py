T = int(input())

count=0
result=[]

for i in range(T):
    arr=list(map(str,input()))
    for j in arr:
        if j=="(":
            count+=1
        else:
            count-=1
            if count<0:
                break
    if count==0:
        result.append('YES')
    else:
        result.append('NO')
    count=0

for i in result:
    print(i)