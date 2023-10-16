from random import randrange
import time
start = time.time()
print(" _   __              _         ___        _        ")
print("| | / /             | |       / _ \      | |       ")
print("| |/ /  ___  ___ ___| | _____/ /_\ \_   _| |_ ___  ")
print("|    \ / _ \/ __/ __| |/ / _ \  _  | | | | __/ _ \ ")
print("| |\  \  __/ (__\__ \   <  __/ | | | |_| | || (_) |")
print("\_| \_/\___|\___|___/_|\_\___\_| |_/\__,_|\__\___/ ")
#keszitunk egy ures listat a vegeredmenyhez
v=[]
# vagyazvan, hogy elore definialom a lehetseges listakat es azt generalom bele a nagylistaba
''' 
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
'''
# vagyaz, hogy elore feltoltom nullakkal es a generalt indexet updatelem 1-esre (v2.0)
lista=[0,0,0]
for i in range(1000):
    lista[randrange(3)]=1
    v.append(lista)
    lista=[0,0,0]
#lista a tippet tartalmazza 
harmas=[1,2,3]
nynv=0 #nyert, nem valtoztatott
nyv=0 #nyert, valtoztatott
vnv=0 #veszitett es nem valtoztatott
vv=0 #veszitett es valtoztatott
for i in range(len(v)):
    #kigeneralunk egy aktualis tippet
    akt=randrange(len(harmas))
    tipp=harmas[akt]
    #kitoroljuk az adott elemet, igy legkozelebb egy n-1 listabol kell generalni csak, valamint nemlehet ujra ugyanazt megadni
    del harmas[akt]
    akt=randrange(len(harmas))
    #a szukitett listabol tippel a showman
    showman=harmas[akt]
    harmas=[1,2,3]
    #megadjuk hogy random valtoztatott-e az ember a tippjen
    valtoztate=randrange(2)
    #kiirjuk, hogy jobban lassunk
    #print(f'vitrinek: {v[i]} | tipp: {tipp} | showman: {showman} | valtoztat-e: {valtoztate}')
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
#vegeredmeny kiirasa        
print(f'nyert,valtoztatott: {nyv}')        
print(f'nyert,NEM valtoztatott: {nynv}')        
print(f'veszitett,valtoztatott: {vv}')        
print(f'veszitett,NEM valtoztatott: {vnv}')        
end = time.time()
#futasido kiirasa
print(f"Time taken: {(end-start)*10**3:.03f}ms")