import os

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}orig.txt')
numz=[]
for l in f:
    numz.append(l.split())
f.close()
    

for i in range(len(numz)):
    for j in range(9):
        print(f'{numz[i][j]}',end=' ')    
    print()

def cenzor(c):
    if c==1:
        print("easy")
    elif c==2:
        print("medium")
    elif c==3:
        print("hard")
    else:
        print("unsolvable")
    return

cenzor(3)


