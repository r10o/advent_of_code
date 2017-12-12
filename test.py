inp=open("day11.dat","r").read().split(",")
pos=[0,0,0]

for i in inp:
    if i == "n" :
        pos=[pos[0]-1,pos[1]+1,pos[2]]
    elif i == "s" :
        pos=[pos[0]+1,pos[1]-1,pos[2]]
    elif i == "ne" :
        pos=[pos[0],pos[1]+1,pos[2]-1]
    elif i == "se" :
        pos=[pos[0]+1,pos[1],pos[2]-1]
    elif i == "nw" :
        pos=[pos[0]-1,pos[1],pos[2]+1]
    elif i == "sw" :
        pos=[pos[0],pos[1]-1,pos[2]+1]


print(pos)
steps=0
while pos!=[0,0,0]:
    start=abs(pos[0])+abs(pos[1])+abs(pos[2])
    if abs(pos[0]-1)+abs(pos[1]+1)+abs(pos[2])< start :
        mbpos=[pos[0]-1,pos[1]+1,pos[2]]
        start=abs(pos[0]-1)+abs(pos[1]+1)+abs(pos[2])

    if abs(pos[0]+1)+abs(pos[1]-1)+abs(pos[2])< start :
        mbpos=[pos[0]+1,pos[1]-1,pos[2]]
        start=abs(pos[0]+1)+abs(pos[1]-1)+abs(pos[2])

    if abs(pos[0])+abs(pos[1]+1)+abs(pos[2]-1)< start :
        mbpos=[pos[0],pos[1]+1,pos[2]-1]
        start=abs(pos[0])+abs(pos[1]+1)+abs(pos[2]-1)

    if abs(pos[0]+1)+abs(pos[1])+abs(pos[2]-1)< start :
        mbpos=[pos[0]+1,pos[1],pos[2]-1]
        start=abs(pos[0]+1)+abs(pos[1])+abs(pos[2]-1)

    if abs(pos[0]-1)+abs(pos[1])+abs(pos[2]+1)< start :
        mbpos=[pos[0]-1,pos[1],pos[2]+1]
        start=abs(pos[0]-1)+abs(pos[1])+abs(pos[2]+1)

    if abs(pos[0])+abs(pos[1]-1)+abs(pos[2]+1)< start :
        mbpos=[pos[0],pos[1]-1,pos[2]+1]
        start=abs(pos[0])+abs(pos[1]-1)+abs(pos[2]+1)
    pos=mbpos
    steps=steps+1

print(steps)
