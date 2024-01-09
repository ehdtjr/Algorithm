n = int(input())

count = 1
j = 0

in_put = []
out_put = []
array = [0]

for _ in range(n):
    num = int(input())
    in_put.append(num)

for i in in_put:
    while 1:
        if array[j] > i:
            print("NO")
            exit(0)
        elif i != array[j]:
            array.append(count)
            j += 1
            count += 1
            out_put.append('+')
        else:
            array.pop()
            if j != 0:
                j -= 1
            out_put.append('-')
            break

for i in out_put:
    print(i)