#base:
#Egy repülőgéppel Európából Amerikába repültünk. Az út során X kilométerenként mértük a felszín tengerszint feletti magasságát. Feltételezésünk szerint ez a magasság mindenhol ≥0. 0 magasságot ott mértünk, ahol tenger van, >0-t pedig ott, ahol szárazföld

#eloszor kigeneraljuk a szinteket (legyen 0-10-ig), a hossz legyen 50, es beleirjuk egy fileba

from random import *
import os

path=os.path.dirname(__file__)
'''
f=open(f'{path}{os.sep}travel.txt','w')

for i in range(50):
    f.write(str(randrange(0,10)))
f.close()
'''
