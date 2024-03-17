import sys
sys.setrecursionlimit(100000)

n=int(sys.stdin.readline())

graph=[0]*n

def attack(a,b):
  for i in range(a):
    if graph[i]==b or abs(a-i)==abs(graph[i]-b):
      return False
  return True

cnt=0

def dfs(x):
  global cnt

  if x==n:
    cnt+=1

  else:
    for i in range(n):
      if attack(x,i):
        graph[x] = i
        dfs(x+1)

dfs(0)

print(cnt)