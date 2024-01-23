N = int(input())

S=input()
count=0
i=2

while len(S)>3:
    i = 2
    while S[i + 1] == '0' or int(S[:i+1])>641:
        i -= 1
    S = S[i + 1:]
    count += 1

if int(S) > 641:
    count += 2

else:
    count += 1

print(count)