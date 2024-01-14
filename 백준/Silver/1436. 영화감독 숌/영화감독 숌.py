N = int(input())

array=[0]

for i in range(666,10000000):
    if str(i).__contains__('666'):
        array.append(i)

print(array[N])