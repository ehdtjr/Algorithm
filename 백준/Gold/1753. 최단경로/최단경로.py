import sys
import heapq

INF=int(1e9)

v,e=map(int,sys.stdin.readline().split())

k=int(sys.stdin.readline().rstrip())

graph=[[]for _ in range(v+1)]
distance=[INF]*(v+1)

for i in range(e):
    start,end,weight=map(int,sys.stdin.readline().split())

    graph[start].append([end,weight])

def dijkstra(k):
    distance[k]=0
    heap=[]

    heapq.heappush(heap,(0,k))

    while heap:
        w,v=heapq.heappop(heap)

        if distance[v]<w:
            continue

        for i in graph[v]:
            next_value=distance[v]+i[1]

            if next_value<distance[i[0]]:
                distance[i[0]]=next_value
                heapq.heappush(heap,(next_value,i[0]))

dijkstra(k)

for i in range(1,len(distance)):
    if distance[i]==1e9:
        print("INF")
    else:
        print(distance[i])