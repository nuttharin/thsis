

import sys
from random import randint

def tobits(val):
	l = [0]*(8)

	l[0]=val & 0x1
	l[1]=(val & 0x2)>>1
	l[2]=(val & 0x4)>>2
	l[3]=(val & 0x8)>>3
	return l

def XOR(a,b):
    return ( (NOT(a)*b) + (a*NOT(b)))

def NOT(val):
	return(val ^ 1)

def AND(a,b):
	return(a*b)

def OR(a,b):
	return(a+b)

def HA(bit1,bit2):
	sum=XOR(bit1,bit2)
	carryout=AND(bit1,bit2)
	return sum,carryout

def FA(bit1,bit2,cin):
	sum1,c1=HA(bit1,bit2)
	sum,c2=HA(sum1,cin)
	carryout=OR(c1,c2)
	return sum,carryout

def cipher(bit,p):
	q=randint(50000, 90000)	
	r=randint(1,200)
	return(  q * p + 2*r +int(bit)),q,r

def cipherX(bit,p):
    r = 150
    q = 0
    q=randint(50000, 90000)	
    return q * p + 2*r +int(bit)


p =randint(3e23, 6e23)*2+1
print(" P : ")
print( 10200 * p + 2* 150 + 1)
val1=13
val2=10

cin=1

v1=[]
v2=[]

v1=tobits(val1)
v2=tobits(val2)
strv1 = ""
strv2 = ""

i = 0 
while i < len(v1) :
  strv1 = strv1 + str(cipherX(v1[i],p))
  i = i +1
print("val1 : " + strv1)

i = 0 
while i < len(v2) :
  strv2 = strv2 + str(cipherX(v2[i],p))
  i = i +1
print("val2 : " + strv2)

de = ""
# Calculating binary value using function
# sum1 = (c_sum1 % p) % 2

sum = bin(int(strv1, 2) + int(strv2, 2))
sumstr = (sum[2:])
print("sum enc : " + sumstr)
i = 0 
while i < len(sumstr) :
  de = de + str((int(sumstr[i]) % p) % 2)
  print(sumstr[i])
  i = i + 1

# Printing result
print("**--**")
print(sumstr)
print(de)



c_carryin,q,r=cipher(cin,p)

cval1b0,q,r=cipher(v1[0],p)
cval2b0,q,r=cipher(XOR(v2[0],c_carryin),p)

cval1b1,q,r=cipher(v1[1],p)
cval2b1,q,r=cipher(XOR(v2[1],c_carryin),p)

cval1b2,q,r=cipher(v1[2],p)
cval2b2,q,r=cipher(XOR(v2[2],c_carryin),p)

cval1b3,q,r=cipher(v1[3],p)
cval2b3,q,r=cipher(XOR(v2[3],c_carryin),p)


c_sum1,c_carryout=FA(cval1b0,cval2b0,c_carryin )
c_sum2,c_carryout=FA(cval1b1,cval2b1,c_carryout )
c_sum3,c_carryout=FA(cval1b2,cval2b2,c_carryout )
c_sum4,c_carryout=FA(cval1b3,cval2b3,c_carryout )

#decrypt

sum1 = (c_sum1 % p) % 2
sum2 = (c_sum2 % p) % 2
sum3 = (c_sum3 % p) % 2
sum4 = (c_sum4 % p) % 2

carryout = (c_carryout % p) % 2


# print("-----Start")
# print("Val1:",val1)
# print("Val2:",val2)
# print("M:",cin)
# if (cin==0): print("Val1+Val2")
# else: print("Val1-Val2")

# print(v1)
# print(v2)

# print("\n-----Results")

# print("Result:\t\t",sum4,sum3,sum2,sum1)
# print("Carry-out:\t",carryout)

# print("\n-----Debug")
# print("CipherSum1:\t",c_sum1)
# print("CipherSum2:\t",c_sum2)
# print("CipherSum3:\t",c_sum3)
# print("CipherSum4:\t",c_sum4)