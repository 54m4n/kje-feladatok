import math
import time
start = time.time()
a=21712
b=10533
f=4

if a<=b:
    kisebb=a
    nagyobb=b
else:
    kisebb=b
    nagyobb=a

print(f'szamok: {a}, {b}')

'''
#--------------------------------------
#lnko rekurzio nelkul
lnko=1
for i in range(1,kisebb+1):
    if nagyobb%i==0 and kisebb%i==0:
        lnko=i
print(f'{nagyobb} es {kisebb} legnagyobb kozos osztoja [rekurzio nelkul]: {lnko}')

#--------------------------------------
#lkkt rekurzio nelkul
lkkt=a*b
for i in range(lkkt,nagyobb-1,-1):
    if (i%nagyobb==0 and i%kisebb==0):
        lkkt=i
print(f'{nagyobb} es {kisebb} legkisebb kozos tobbszorose [rekurzio nelkul]: {lkkt}')        

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
#--------------------------------------
#lkkt rekurzioval
def lkkt(a,b):
    lk=a*b / lnko(a,b)
    return lk
print(f'{nagyobb} es {kisebb} legkisebb kozos tobbszorose [rekurzioval]: {"%.1d" % lkkt(a,b)}')        

# faktorialis rekurzioval
def fak(f):
    if f==0:
        return(1)
    else:
        return(fak(f-1)*f)

print(f'{f} faktorialis [rekurzioval]: {fak(f)}')




end = time.time()
print(f"Time taken: {(end-start)*10**3:.03f}ms")