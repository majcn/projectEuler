#!/usr/bin/python2

def getNewCoords(d, x, y):
    if d == 0:
        return x,y+1
    if d == 1:
        return x+1,y
    if d == 2:
        return x,y-1
    if d == 3:
        return x-1,y

SIZE=1001
t = [[0 for i in range(SIZE)] for i in range(SIZE)]
c = 1

posx, posy, posd = SIZE/2, SIZE/2, 0
t[posx][posy] = c
c+=1
for i in range(SIZE*SIZE-1):
    while t[posx][posy] != 0:
        posx, posy = getNewCoords(posd, posx, posy)
    td = (posd+1)%4
    tx, ty = getNewCoords(td, posx, posy)
    if t[tx][ty] == 0:
        posd = td
    t[posx][posy] = c
    c += 1

print sum([t[i][j] for i in range(SIZE) for j in range(SIZE) if i==j or SIZE-1-i==j])

