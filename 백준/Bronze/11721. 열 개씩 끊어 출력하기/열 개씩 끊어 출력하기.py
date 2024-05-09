import sys

string=sys.stdin.readline().rstrip()

count=0

for s in string:
    if count==10:
        print()
        count=0
        
    print(s,end='')
    count+=1