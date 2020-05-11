import numpy as np

jatek=np.array([["E","E","E"],["E","E","E"],["E","E","E"]])
hiba=1
dontetlen="igen"

for i in range (3):
    for j in range (3):
        print("jatek[",i,",",j,"]=")
        jatek[i,j]=input("")
print ("A játek így néz ki:")
print (jatek)
for i in range (3):
    for j in range (3):
        if jatek[i,j]!="X" and jatek[i,j]!="O" and jatek[i,j]!="E":
            hiba = 0
if hiba==0:
    print("Hiba: csak NAGY 'X','O' es 'E'-t használhatsz!")
else:
    print ("Végeredmény: ")
    if jatek[0,0]==jatek[0,1]==jatek[0,2] and jatek[0,0]!="E":
        print (jatek[0,0])
        dontetlen = "nem"
    elif jatek[1,0]==jatek[1,1]==jatek[1,2] and jatek[1,0]!="E":
        print (jatek[1,0])
        dontetlen = "nem"
    elif jatek[2,0]==jatek[2,1]==jatek[2,2] and jatek[2,0]!="E":
        print (jatek[2,0])
        dontetlen = "nem"
    elif jatek[0,0]==jatek[1,0]==jatek[2,0] and jatek[0,0]!="E":
        print (jatek[0,0])
        dontetlen = "nem"
    elif jatek[0,1]==jatek[1,1]==jatek[2,1] and jatek[0,1]!="E":
        print (jatek[0,1])
        dontetlen = "nem"
    elif jatek[0,2]==jatek[1,2]==jatek[2,2] and jatek[0,2]!="E":
        print (jatek[0,2])
        dontetlen = "nem"
    elif jatek[0,0]==jatek[1,1]==jatek[2,2] and jatek[0,0]!="E":
        print (jatek[0,0])
        dontetlen = "nem"
    elif jatek[0,2]==jatek[1,1]==jatek[2,0] and jatek[0,2]!="E":
        print (jatek[0,2])
        dontetlen = "nem"
    if dontetlen=="igen":
        print ("Egyenlő")
