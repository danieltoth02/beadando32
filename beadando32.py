import numpy as np
lista=["E","X","O"]                                                     
jatek=np.random.choice(lista,(3,3))                                  
print (jatek)
if jatek[0,0]==jatek[0,1]==jatek[0,2] and jatek[0,0]!="E":
    print (jatek[0,0])
if jatek[1,0]==jatek[1,1]==jatek[1,2] and jatek[1,0]!="E":
    print (jatek[1,0])
if jatek[2,0]==jatek[2,1]==jatek[2,2] and jatek[2,0]!="E":
    print (jatek[2,0])
if jatek[0,0]==jatek[1,0]==jatek[2,0] and jatek[0,0]!="E":
    print (jatek[0,0])
if jatek[0,1]==jatek[1,1]==jatek[2,1] and jatek[0,1]!="E":
    print (jatek[0,1])
if jatek[0,2]==jatek[1,2]==jatek[2,2] and jatek[0,2]!="E":
    print (jatek[0,2])
if jatek[0,0]==jatek[1,1]==jatek[2,2] and jatek[0,0]!="E":
    print (jatek[0,0])
if jatek[0,2]==jatek[1,1]==jatek[2,0] and jatek[0,2]!="E":
    print (jatek[0,2])
else:
    print ("egyenlo")
