from random import randrange
print(" _   __              _         ___        _        ")
print("| | / /             | |       / _ \      | |       ")
print("| |/ /  ___  ___ ___| | _____/ /_\ \_   _| |_ ___  ")
print("|    \ / _ \/ __/ __| |/ / _ \  _  | | | | __/ _ \ ")
print("| |\  \  __/ (__\__ \   <  __/ | | | |_| | || (_) |")
print("\_| \_/\___|\___|___/_|\_\___\_| |_/\__,_|\__\___/ ")

v=[]
v1=[0,0,1]
v2=[0,1,0]
v3=[1,0,0]

for i in range(1000):
    choose=randrange(3)
    if choose==0:
        v.append(v1)
    if choose==1:
        v.append(v2)
    if choose==2:
        v.append(v3)


harmas=[1,2,3]

nynv=0 #nyert, nem valtoztatott
nyv=0 #nyert, valtoztatott
vnv=0 #veszitett es nem valtoztatott
vv=0 #veszitett es valtoztatott

for i in range(len(v)):
    akt=randrange(len(harmas))
    tipp=harmas[akt]
    del harmas[akt]
    akt=randrange(len(harmas))
    showman=harmas[akt]
    harmas=[1,2,3]
    valtoztate=randrange(2)
    print(f'vitrinek: {v[i]} | tipp: {tipp} | showman: {showman} | valtoztat-e: {valtoztate}')
    if valtoztate==1:
        tipp=showman
        
    if ((v[i].index(0)+1)==tipp) and valtoztate==0:
        nynv=nynv+1
    if ((v[i].index(0)+1)==tipp) and valtoztate==1:
        nyv=nyv+1
    if ((v[i].index(0)+1)!=tipp) and valtoztate==0:
        vnv=vnv+1
    if ((v[i].index(0)+1)!=tipp) and valtoztate==1:
        vv=vv+1
        
print(f'nyert,valtoztatott: {nyv}')        
print(f'nyert,NEM valtoztatott: {nynv}')        
print(f'veszitett,valtoztatott: {vv}')        
print(f'veszitett,NEM valtoztatott: {vnv}')        
    