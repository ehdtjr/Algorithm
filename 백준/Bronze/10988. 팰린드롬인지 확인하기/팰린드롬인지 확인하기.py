import sys

s=sys.stdin.readline().rstrip()

if s[0:]==s[len(s)::-1]:
    print('1')
else:
    print('0')

