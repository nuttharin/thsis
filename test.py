import mysql.connector
import random
from decimal import *

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

# p=10000000000000000001   #key
p = 1000000000000003973
l = 20
q=random.randint(3, 100)
r=random.randint(3, 10)


mycursor = mydb.cursor()
query = "SELECT  SUM(t1.TempHighF) , SUM(t1.TempAvgF) , SUM(t1.TempLowF) FROM ( SELECT * FROM `DGHV`.`austin_weather` LIMIT 20 ) as t1"
mycursor.execute(query)

myresult = mycursor.fetchall()
for x in myresult:
  print(x)


query = "SELECT  SUM(t1.TempHighF) , SUM(t1.TempAvgF) , SUM(t1.TempLowF) FROM ( SELECT * FROM `DGHV`.`austin_weather_enc` LIMIT 20 ) as t1"
mycursor.execute(query)

myresult = mycursor.fetchall()
for x in myresult:
    print(x)
    for y in x:            
        d = ((y % p) % power(2,l) ) /1000
        print(d)