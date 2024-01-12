N, M = map(int, input().split())

array = []
a=b=0
result = []

for _ in range(N):
    n = input()
    array.append(n)

for k in range(0, N - 7):
    for l in range(0, M - 7):
         for i in range(k, k + 8):
             for j in range(l, l + 8):
                     if (i + j) % 2 == 0:
                         if array[i][j] != 'W':
                             a+=1
                         elif array[i][j] != 'B':
                             b+=1
                     else:
                         if array[i][j]!='B':
                             a+=1
                         elif array[i][j] != 'W':
                             b+=1
         result.append(min(a,b))
         a=b=0

print(min(result))