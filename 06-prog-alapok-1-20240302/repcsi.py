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

part=[]
for i in range(len(measure)):
    if measure[i]==0:
        part.append(i)
max=0
for i in range(len(part)):
    try:
        if part[i+1]-part[i]>=max:
            max=part[i+1]-part[i]
            balpart=part[i]
            jobbpart=part[i+1]
    except:
        IndexError
print('01:')
print(f'legszelesebb sziget bal es jobb partja: {balpart} es {jobbpart}')

#02.
#Készíts programot, amely meghatározza a legmagasabb hegycsúcsot tartalmazó sziget bal-, illetve jobboldali partját!
#mivel a szigeteink koordinatai mar megvannak, a koztes allapotot vizsgalom le max-ra

max=0

for  i in range(len(part)):
    try:
        for j in range(part[i+1]-part[i]):
            if measure[part[i]+j]>=max:
                max=measure[part[i]+j]
                bal=part[i]
                jobb=part[i+1]
    except:
        IndexError
print('02:')
print(f'legmagasabb hegycsucsot tartalmazo sziget bal es jobb partja: {bal}, {jobb}')

#03.
#Készíts programot, amely meghatározza a legmagasabb csúcsot, ami valamelyik földrészen található!
#lenyegeben a legmagasabb csucsot keressuk, mindegy, hogy sziget vagy nemsziget csak ne tenger legyen
max=0
for i in range(len(measure)):
    if measure[i]>=max:
        max=measure[i]
print('03:')
print(f'a legmagasabb csucs ever: {max}')

print(part)