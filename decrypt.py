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
p = 1000000000000000000000000000000000000000000000000000000001
# p = 1000000000000000000001 #key //22
# p = 100000000000000001  # // 18
# p = 1000000000000001  # 16
# p = 10000000000001  # 14
# p = 100000000001 
# 1000000000000000000000000000000000000000000000000000000001
l = 64
q=random.randint(3, 100)
r=random.randint(3, 10)


mycursor = mydb.cursor()
query = "SELECT  SUM(t1.TempHighF) , SUM(t1.TempAvgF) , SUM(t1.TempLowF) FROM ( SELECT * FROM `DGHV`.`austin_weather_test_20000` LIMIT 1,2) as t1"
mycursor.execute(query)

myresult = mycursor.fetchall()
for x in myresult:
  print(x)


query = "SELECT  SUM(t1.TempHighF) , SUM(t1.TempAvgF) , SUM(t1.TempLowF) FROM ( SELECT * FROM `DGHV`.`austin_weather_enc_20000` LIMIT 1,2) as t1"
mycursor.execute(query)

myresult = mycursor.fetchall()

tempSum = 0 
for x in myresult:
    print(x)
    for y in x:            
        temp = math.floor(y/p)
        # print("Temp : " , temp)  
        # print(temp * p % p % power(2,l)/1000)  
        print(y - (temp * p))
        print( (y - (temp * p)) % p % power(2,l)/1000)     
        # print(((p*temp)% power(2,l)/1000) + ((y-p*temp)% power(2,l)/1000))
        d = ((y % p) % power(2,l) ) /1000
        print(d)
        # d = ((y % p) % power(2,l) ) /1000
        # print(d)

# print(161063839440000% p)
# 1073741824
