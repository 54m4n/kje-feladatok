import os

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}lottoszamok.txt','r')
lines=f.readlines()
f.close()

szamok=[]
ujlista=[]


tippek=[]
for i in range(5):
    tippek.append(int(input(f'{i+1}. tipp: ')))

stat=[0,0,0,0,0]
nemvolt=0

for szamok in lines:
    ujlista.append(szamok.split(","))

sorsolasokszama=len(ujlista)

for i in range(sorsolasokszama):
    talalat=0
    tmptalalat=[]
    for j in range(5):
        aktszam=int(ujlista[i][j].strip())
        if aktszam in tippek:
            talalat=talalat+1
            tmptalalat.append(aktszam)        
    if talalat>0:
        print(f'{i+1}. sorsolason talalatok szama: {talalat}, meghozza: {tmptalalat}')            
        stat[talalat-1]=stat[talalat-1]+1
    else:
        print(f'{i+1}. sorsolason nem volt talalat.')
        nemvolt=nemvolt+1
        
    

print("---STAT---")
print(f'tippek tehat: {tippek}')
print(f'{stat[4]} db 5-os talalat')
print(f'{stat[3]} db 4-es talalat')
print(f'{stat[2]} db 3-as talalat')
print(f'{stat[1]} db 2-es talalat')
print(f'{stat[0]} db 1-es talalat')
print(f'{nemvolt} db alkalommal nem volt talalat')
print("----------")