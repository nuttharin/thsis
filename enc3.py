
import mysql.connector
import random
from decimal import *
import math


def power(base, exponent):
    # Base Case
    if exponent == 0 :
        return 1
    
    # Recursive Case
    else :
        return base * power(base, exponent - 1)


# p=10000000000000000000000000000001   #key
p=1000000000000000000000000000000000000000000000000000000000000001 
l = 64
q=random.randint(3, 100)
r=random.randint(3, 10)
i=9223372036854775806
# 740000000000000000000027917287490  // 33
# 2147483647 // 32 int
# 9223372036854775807 // 64 int
while i <= 9223372036854775807 :
    m = i
    c = p * q + power(2,l) * r + m
    d = (c % p) % power(2,l)
    print(str(m) +" : "+ str(d) + " : " + str(c))

    if d != m :
        break

    i = i + 1


    26000000000000000000000000000000000000000000138350580552821637145




    100000000000000000000
    6000000000000000000
    100000000000000000000
    4800000000000000000
    45990000000000000000
    3000000000000000000