import sys
sys.setrecursionlimit(10**5)

tree = []

while True:
    try:
        tree.append(int(sys.stdin.readline()))
    except:
        break

def dfs(start,end):
    if start>end:
        return

    idx=end+1

    for i in range(start,end+1):
        if tree[start]<tree[i]:
            idx=i
            break

    dfs(start+1,idx-1)
    dfs(idx,end)
    print(tree[start])

dfs(0,len(tree)-1)
