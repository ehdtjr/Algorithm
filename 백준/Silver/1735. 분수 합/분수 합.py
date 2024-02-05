A, B = map(int, input().split())
C, D = map(int, input().split())

A = A * D
C = C * B

chi = A + C
par = B * D

def mul(chi, par):
    while True:
        if chi % par == 0:
            return chi, par
        else:
            chi = chi % par

        if par % chi == 0:
            return chi, par
        else:
            par = par % chi


a, b = mul(chi, par)

while True:
    if min(a, b) == 1:
        print(int(chi),int (par))
        break
    else:
        chi = chi / min(a, b)
        par = par / min(a, b)
        a, b = mul(chi, par)