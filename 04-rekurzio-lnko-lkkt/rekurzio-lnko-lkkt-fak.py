import math
'''
# rekurziv legkisebb kozos tobbszoros a legnagyobb kozos oszto es a pszeudokod alapjan

def lnko(a,b):
    if (a==b):
        ln=a
    if (a<b):
        ln = lnko(a, b-a)
    if (a>b):
        ln = lnko(a-b, b)

    return ln


def lkkt(a,b):
    lk=a*b / lnko(a,b)
    return lk

print(lnko(10,3))
print("%.1d" % lkkt(10,3))

# rekurziv faktorialis

def fak(n):
    print(n)
    if n==0:
        return(1)
    else:
        return(fak(n-1)*n)

print(fak(4))
'''

#lnko rekurzio nelkul
a=15
b=10
lnko=1
if a<=b:
    kisebb=a
    nagyobb=b
else:
    kisebb=b
    nagyobb=a

for i in range(math.floor(kisebb/2),kisebb+1):
    if nagyobb%i==0 and kisebb%i==0:
        lnko=i
print(f'{nagyobb} es {kisebb} legnagyobb kozos osztoja: {lnko}')

#lkkt rekurzio nelkul
a=5
b=9
lkkt=a*b
if a<=b:
    kisebb=a
    nagyobb=b
else:
    kisebb=b
    nagyobb=a

for i in range(math.floor(kisebb/2),kisebb+1):
    if nagyobb%i==0 and kisebb%i==0:
        lnko=i
print(f'{nagyobb} es {kisebb} legnagyobb kozos osztoja: {lnko}')



