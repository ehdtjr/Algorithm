import sys

sum=0

for i in range(5):
    n=int(sys.stdin.readline().rstrip())

    if n < 40:
        sum+=40
    else:
        sum+=n
print(sum//5)