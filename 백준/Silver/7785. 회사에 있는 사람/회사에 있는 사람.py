import sys

n = int(sys.stdin.readline())

arr=[]
d={}

for i in range(n):
    x,y=map(str,sys.stdin.readline().split())
    if y=="enter":
        d[x]=y
    else:
        del d[x]

print('\n'.join(sorted(d.keys(),reverse=True)))