#!/usr/bin/python2
f = [[int(j) for j in i.replace('\n','').split(" ")] for i in open('18.input').readlines()]

G = {}
for i in range(len(f)-1):
    for j in range(len(f[i+1])-1):
        G[str(i)+'_'+str(j)] = {str(i+1)+'_'+str(j): 100000000-f[i+1][j], str(i+1)+'_'+str(j+1): 100000000-f[i+1][j+1]}
for i in range(len(f)):
    G[str(len(f)-1)+"_"+str(i)] = {}


start = '0_0'
goals = [str(len(f)-1)+"_"+str(i) for i in range(len(f))]

openset = [start]

g_score = {}
g_score[start] = 100000000-f[0][0]

while openset:
    current = min(openset, key = lambda node: g_score[node])
    if current in goals:
        print 1500000000-g_score[current]
        break
    openset.remove(current)
    for neighbor in G[current]:
        tentative_g_score = g_score[current] + G[current][neighbor]
        if (neighbor not in openset) or (tentative_g_score <= g_score[neighbor]):
            g_score[neighbor] = tentative_g_score
            if neighbor not in openset:
                openset.append(neighbor)
