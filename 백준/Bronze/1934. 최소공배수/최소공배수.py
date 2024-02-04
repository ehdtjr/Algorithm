T = int(input())

for i in range(T):
    A,B=map(int,input().split())
    a,b=A,B
    while True:
        if A%B==0:
            break
        else:
            A=A%B
        if B%A==0:
            break
        else:
            B=B%A

    print((a*b)//min(A,B))