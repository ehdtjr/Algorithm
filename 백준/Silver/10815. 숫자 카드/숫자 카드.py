N = int(input())
card = set(map(int,input().split()))
M = int(input())
compare = list(map(int,input().split()))
for i in compare:
    if i in card:
        print(1,end=' ')
    else:
        print(0,end=' ')