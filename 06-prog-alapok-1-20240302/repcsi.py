#base:
#Egy repülőgéppel Európából Amerikába repültünk. Az út során X kilométerenként mértük a felszín tengerszint feletti magasságát. Feltételezésünk szerint ez a magasság mindenhol >=0. 0 magasságot ott mértünk, ahol tenger van, >0-t pedig ott, ahol szárazföld

#eloszor kigeneraljuk a szinteket (legyen 0-10-ig), a meres legyen 50, es beleirjuk egy fileba

from random import *
import os

path=os.path.dirname(__file__)
'''
f=open(f'{path}{os.sep}travel.txt','w')

for i in range(50):
    f.write(str(randrange(0,10)))
f.close()
'''

#beolvassuk a file tartalmat egy stringbe
f=open(f'{path}{os.sep}travel.txt','r')
for i in f:
    travel=i

#atalakitjuk tombbe es int-e is, mert matematikai muveleteket stringgel nemtudunk (de igen amugy) vegezni:
measure=[]
for i in range(len(travel)):
    measure.append(int((travel[i:i+1:1])))
f.close()

#01.
#Készíts programot, amely meghatározza a legszélesebb sziget bal-, illetve jobboldali partját!
#komment: sziget akkor van, ha a ket oldala 0. ezek kozul kell a maxot kivalasztani
max=0
count=0
for i in range(len(measure)):
    if measure[i]!=0:
        count=count+1
    else:
        count=0
    if count>=max:
        max=count
print(f'legszelesebb sziget: {max}')
