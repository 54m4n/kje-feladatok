import os

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}s.txt')
numz=[]
for l in f:
    numz.append(l.split())
f.close()
    

for i in range(len(numz)):
    for j in range(9):
        print(numz[i][j],end=' ')
    print()
