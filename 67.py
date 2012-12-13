#!/usr/bin/python2
import heapq

MAX_SUM=100000000

f = [[int(j) for j in i.replace('\n','').split(" ")] for i in open('67.input').readlines()]

G = {}
for i in range(len(f)-1):
    for j in range(len(f[i+1])-1):
        G[str(i)+'_'+str(j)] = {str(i+1)+'_'+str(j): MAX_SUM-f[i+1][j], str(i+1)+'_'+str(j+1): MAX_SUM-f[i+1][j+1]}
for i in range(len(f)):
    G[str(len(f)-1)+"_"+str(i)] = {}


start = '0_0'
goals = set(str(len(f)-1)+"_"+str(i) for i in range(len(f)))

openset = set()
openset.add(start)

openHeap = []
openHeap.append((MAX_SUM-f[0][0], start))

while openset:
    g_score, current = heapq.heappop(openHeap)
    if current in goals:
        print len(f)*MAX_SUM-g_score
        break
    openset.remove(current)
    for neighbor in G[current]:
        if neighbor not in openset:
            openset.add(neighbor)
            heapq.heappush(openHeap, (g_score + G[current][neighbor], neighbor))
