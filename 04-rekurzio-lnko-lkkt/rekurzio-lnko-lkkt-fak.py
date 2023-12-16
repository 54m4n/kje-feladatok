import math
import time
from turtle import *
start = time.time()
a=18900
b=2115
f=8

if a<=b:
    kisebb=a
    nagyobb=b
else:
    kisebb=b
    nagyobb=a

print(f'szamok [lnko/lkkt]: {a}, {b}')
print(f'szam [fakt]: {f}')

'''
#--------------------------------------
#lnko rekurzio nelkul
lnko=1
for i in range(1,kisebb+1):
    if nagyobb%i==0 and kisebb%i==0:
        lnko=i
print(f'{nagyobb} es {kisebb} legnagyobb kozos osztoja [rekurzio nelkul]: {lnko}')
'''
'''
#--------------------------------------
#lnko rekurzioval
def lnko(a,b):
    if (a==b):
        ln=a
    if (a<b):
        ln = lnko(a, b-a)
    if (a>b):
        ln = lnko(a-b, b)
    return ln
print(f'{nagyobb} es {kisebb} legnagyobb kozos osztoja [rekurzioval]: {lnko(a,b)}')
'''

'''
#--------------------------------------
#lkkt rekurzio nelkul
lkkt=a*b
for i in range(lkkt,nagyobb-1,-1):
    if (i%nagyobb==0 and i%kisebb==0):
        lkkt=i
print(f'{nagyobb} es {kisebb} legkisebb kozos tobbszorose [rekurzio nelkul]: {lkkt}')        
'''

'''
#--------------------------------------
#lkkt rekurzioval
def lkkt(a,b):
    lk=a*b / lnko(a,b)
    return lk
print(f'{nagyobb} es {kisebb} legkisebb kozos tobbszorose [rekurzioval]: {"%.1d" % lkkt(a,b)}')        
'''

'''
#--------------------------------------
# faktorialis rekurzio nelkul
fakt = 1
for i in range(1, f+1):
    fakt = fakt * i
print(f'{f} faktorialis [rekurzio nelkul]: {fakt}')
'''
'''
#--------------------------------------
# faktorialis rekurzioval
def fak(f):
    if f==0:
        return(1)
    else:
        return(fak(f-1)*f)

print(f'{f} faktorialis [rekurzioval]: {fak(f)}')
'''

'''
#--------------------------------------
# koch
def koch(h, sz):
  if sz == 0:
    forward(h)
  else:
    koch(h, sz-1)
    left(60)
    koch(h, sz-1)
    right(120)
    koch(h, sz-1)
    left(60)
    koch(h, sz-1)
reset()
koch(20,40)
done()
'''

'''
#--------------------------------------
# spiral
def spiral(h,sz):
  if sz < 0:
    left(90)
  else:
    forward(h)
    left(90)
    spiral(h+10,sz-0.5)

reset()
spiral(10,10)
done()
'''


end = time.time()
print(f"Time taken: {(end-start)*10**3:.03f}ms")