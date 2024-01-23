n = int(input())

arr=[]
d={}

for i in range(n):
    x,y=map(str,input().split())
    if y=="enter":
        d[x]=y
    else:
        del d[x]

print('\n'.join(sorted(d.keys(),reverse=True)))