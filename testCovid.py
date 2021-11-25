import mysql.connector
import random
from decimal import *
import math

print("Start !! \n")

mydb = mysql.connector.connect(
    host="158.108.207.221",
    user="admin1",
    password="51451340",
    database="DGHV"
)

# print(mydb)

def power(base, exponent):
    # Base Case
    if exponent == 0 :
        return 1
    
    # Recursive Case
    else :
        return base * power(base, exponent - 1)
p = 1000000000000000000000000000000000000000000000000000000000000001
# p = 1000000000000000000001 #key //22
# p = 100000000000000001  # // 18
# p = 1000000000000001  # 16
# p = 10000000000001  # 14
# p = 100000000001 
# 1000000000000000000000000000000000000000000000000000000001
l = 64
q= 99
r= 251314668

        #  18446744073709551576
mMaxint= 9223372036854775807 
cMaxint = p * q + power(2,l) * r + mMaxint

mycursor = mydb.cursor()
query = "SELECT  SUM(t1.New_cases) , SUM(t1.Cumulative_cases) , SUM(t1.New_deaths) ,SUM(t1.Cumulative_deaths) FROM ( SELECT * FROM `DGHV`.`WHO-COVID-19-global-data` LIMIT 1,2) as t1 "
mycursor.execute(query)

myresult = mycursor.fetchall()
for x in myresult:
  print(x)


query = "SELECT  SUM(t1.New_cases) , SUM(t1.Cumulative_cases) , SUM(t1.New_deaths) ,SUM(t1.Cumulative_deaths) FROM ( SELECT * FROM `DGHV`.`WHO-COVID-19` LIMIT 1,2) as t1 "
mycursor.execute(query)

myresult = mycursor.fetchall()

tempSum = 0 
for x in myresult:
    print(x)
    for c in x:            
        temp = math.floor(c/cMaxint) 
        print(temp)
        # print((c-(temp*cMaxint)))
        print(((c-(temp*cMaxint)) % p % power(2,l)) / 1000)
        print(((c-(temp*cMaxint)) % p % power(2,l) + ((temp*mMaxint))) / 1000)
        d = ((c % p) % power(2,l) )
        print(d)
        d = ((d % p) % power(2,l) )
        print(d)
        # d = c - cMaxint
        print(d)
        d = ((d % p) % power(2,l) )
        print(d)
        print("-----------------------------------------------------")

# print(161063839440000% p)
# 1073741824
