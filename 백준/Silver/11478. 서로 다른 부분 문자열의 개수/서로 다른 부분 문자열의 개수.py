S = input()

l=len(S)
s=set()

for i in range(1,l+1):
    j=0
    while i<l:
        s.add(S[j:i])
        j+=1
        i+=1
    s.add(S[j:])

print(len(s))