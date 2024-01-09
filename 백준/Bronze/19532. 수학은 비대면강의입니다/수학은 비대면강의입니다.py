a, b, c, d, e, f = map(int, input().split())
x = y = 0

if a==0:
    y=c/b
    e=e*int(y)
    f = f - e
    x = f / d
elif d==0:
    y=f/e
    b = b * int(y)
    c = c - b
    x = c / a
elif b==0:
    x=c/a
    d = d * int(x)
    f = f - d
    y = f / e
elif e==0:
    x=f/d
    a = a * int(x)
    c = c - a
    y = c / b
else:
    l = a
    r = d

    a = a * r
    b = b * r
    c = c * r

    d = d * l
    e = e * l
    f = f * l

    if a == d:
        y = (c - f) / (b - e)
    else:
        y = (c + f) / (b + e)

    y = int(y)
    b = b * y

    c = c - b

    x = c / a
    x = int(x)

print(int(x),int(y), end=' ')