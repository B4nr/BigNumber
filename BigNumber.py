import math
from decimal import *
import time

st=time.time()
getcontext().prec=50000000
irrational = Decimal(2).sqrt()
print(irrational)
irrational = str(irrational)
et=time.time()
tt=st-et
tt=str(tt)

file = open("squareroot2.txt", "w")
file.write(tt)
file.write(irrational)
file.close()