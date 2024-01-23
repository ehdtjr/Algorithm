#7785
import sys
n = int(sys.stdin.readline())
log = dict()
for _ in range(n):
    name, status = sys.stdin.readline().split()
    if status == 'enter':
        log[name] = True
    else:
        del log[name] #O(1)
print('\n'.join(sorted(log.keys(), reverse = True)))