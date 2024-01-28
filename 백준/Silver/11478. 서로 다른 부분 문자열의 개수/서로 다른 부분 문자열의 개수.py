S = input()

l=len(S)
arr=[]

for i in range(1,l+1):
    j=0
    while i<l:
        arr.append(S[j:i])
        j+=1
        i+=1
    arr.append(S[j:])


print(len(set(arr)))