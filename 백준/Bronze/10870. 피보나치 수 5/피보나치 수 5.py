import sys
sys.setrecursionlimit(10**6)

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

n=int(sys.stdin.readline().rstrip())

print(fib(n))