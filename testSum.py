
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
l = 63
# print(power(2,l))
# q=random.randint(3, 100)
# r=random.randint(3, 100000000000000)
q= 99
r= 9223372036854775806
i=1
# 740000000000000000000027917287490  // 33
# 2147483647 // 32 int
# 9223372036854775807 // 64 int
maxint = p * q + power(2,l) * r + 9223372036854775807
mMaxint= 9223372036854775807 
m = 9223372036854775807
# c= 85899345920000000000000000000000000000000000356526731324810973379855122432
c = p * q + power(2,l) * r + m
sum = 0
sumD = 0
tempSum = 0 
b = 0

print(  ( 99000000000000000000000000085070591730234615856620279821087277154  % p) % power(2,l))
while i <= 10 :
    # q=random.randint(3, 100)
    # r=random.randint(3, 100000000000000)
    cMaxint = p * q + power(2,l) * r + mMaxint
   
    # while c > maxint :
    #     print(1)
    #     c = c - maxint
    #     print((maxint % p) % power(2,l))
    #     sum = sum + ((maxint % p) % power(2,l))
    # sum = sum + (c % p) % power(2,l)
    # print(str(m) +" : "+ str(sum) + " : " + str(c))
    d = (c % p) % power(2,l)
    sum = sum + d
    sumD = sumD + m
    print(str(m) +" : "+ str(d) + " : " + str(c) + " : " + str(len(str(c)))  )
    print(sumD)
    print((sum % p) % power(2,l))
    temp = math.floor(c/cMaxint) 
    print((c-(temp*cMaxint)) % p % power(2,l) + ((temp*mMaxint)))

    tempSum = sum
    # while mMaxint < (m % p) % power(2,l) :
    #     print(1)
    #     tempSum = m - mMaxint
    #     b = b + mMaxint
    #     # print((maxint % p) % power(2,l))
    #     d = d + 9223372036854775807
    # b = 
    # d = (c % p) % power(2,l)
    # sum = sum + d
    # sumD = sumD + m
    # print(str(m) +" : "+ str(d) + " : " + str(c))
    # print(sumD)
    # print((sum % p) % power(2,l))
   

    d = d + (tempSum % p) % power(2,l)
    # print(str(d))

    print("------------------------")
   
    # temp = math.floor(c/p)
    # print("Temp : " , temp)  
    # print(temp * p % p % power(2,l)/1000)  
    # print(c - (temp * p))
    # print( (c - (temp * p)) % p % power(2,l))     
    # print(((p*temp)% power(2,l)/1000) + ((y-p*temp)% power(2,l)/1000))
    # d = ((c % p) % power(2,l) ) /1000
    # print(d)

    c = c + c
    
    m = m + m
    # c = p * q + power(2,l) * r + m
    i = i + 1


    # 10621454118062000000
    # 9223372036854775807
    # 5310727061504000000
    # 21242908241070000000

# 99000000000000000000000000000000000004635937362565283492804310587
# 99000000000000000000000000085070591730234615856620279821087277154