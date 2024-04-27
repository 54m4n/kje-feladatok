import os
from random import *

cucc=[]

for i in range(100):
    cucc.append(randrange(0,100))
    
for i in range(len(cucc)):
    print(cucc.count(i))