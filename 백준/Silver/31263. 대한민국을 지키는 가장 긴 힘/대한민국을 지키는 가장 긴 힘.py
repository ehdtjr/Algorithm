N = int(input())

S=input()
count=0
i=2

while S:
    if len(S)>3:
        i=2
        while S[i+1]=='0':
            i-=1
        S=S[i+1:]
        count+=1
    else:
        if int(S)>641:
            count+=2
            break
        else:
            count+=1
            break

print(count)