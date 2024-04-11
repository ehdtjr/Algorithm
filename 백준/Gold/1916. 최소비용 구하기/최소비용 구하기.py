import sys
import heapq

INF=int(1e9)

n=int(sys.stdin.readline().rstrip())
m=int(sys.stdin.readline().rstrip())

graph=[[]for _ in range(n+1)]
distance=[INF]*(n+1)

for i in range(m):
    start,end,weight=map(int,sys.stdin.readline().split())
    graph[start].append([end,weight])

start,end=map(int,sys.stdin.readline().split())

def dijkstra(start):
    heap=[]
    distance[start]=0

    heapq.heappush(heap,(0,start))

    while heap:
        weight,node=heapq.heappop(heap)

        if distance[node]<weight:
            continue

        for i in graph[node]:
            next_val=i[1]+weight

            if next_val < distance[i[0]]:
                distance[i[0]]=next_val
                heapq.heappush(heap,(next_val,i[0]))

dijkstra(start)

print(distance[end])