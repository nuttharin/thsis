# INSERT INTO `DGHV`.`WHO-COVID-19-global-data`(`Date_reported`, `Country_code`, `Country`, `WHO_region`, `New_cases`, `Cumulative_cases`, `New_deaths`, `Cumulative_deaths`) VALUES ('1/3/2020', 'AF', 'Afghanistan', 'EMRO', 0, 0, 0, 0);
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
l = 64
q= 99
r= 251314668


mycursor = mydb.cursor()
# query = "SELECT * FROM `DGHV`.`austin_weather` LIMIT 0,100"
query = "SELECT t2.id , t2.soil1 , t2.soil2 ,t2.bat , t2.dataTime FROM ( SELECT t.*, @rownum := @rownum + 1 AS rn FROM `IoT.Input.SinghaS1.17` as t , (SELECT @rownum := 0) r ) t2 WHERE t2.rn BETWEEN 1 AND 100000"
# query = "SELECT * FROM `WHO-COVID-19-global-data`"

mycursor.execute(query)

myresult = mycursor.fetchall()
print(len(myresult))
print(myresult)
print(myresult[1])
# INSERT INTO `DGHV`.`IoT.Input.SinghaS1.17_20000`(`id`, `soil1`, `soil2`, `bat`, `dataTime`) VALUES ('1', 1, 1, 1, '1')
query2 = "INSERT INTO `DGHV`.`IoT.Input.SinghaS1.17_raw_100000`(`id`, `soil1`, `soil2`, `bat`, `dataTime`) VALUES  "
queryValue = ""
arrM = []
j = 0
countx = 1

for x in myresult:
    # c = p*q + power(2,l) *r +m    
    i = 0 
    while i < len(x) :       
        arrM.append(x[i])        
        i = i + 1

    txt = "('{}', {},{},{}, '{}')"   
    txt = txt.format(str(arrM[0]),str(arrM[1]),str(arrM[2]),str(arrM[3]),str(arrM[4]))
    print(str(countx)+" ==== "+txt)
    queryValue = queryValue + txt
    if j < len(myresult) -1 :
        queryValue =  queryValue + " , " 
    txt = ""
    arrM = []
    # print(queryValue)
    j=j+1
    countx = countx + 1
query2 = query2 + queryValue 


mycursor = mydb.cursor()


mycursor.execute(query2)

mydb.commit()

print(mycursor.rowcount, "record inserted.")





# mycursor1 = mydb.cursor()

# query = "SELECT * FROM `IoT.Input.SinghaS1.17` LIMIT 60001,80000"
# # query = "SELECT * FROM `WHO-COVID-19-global-data`"

# mycursor1.execute(query)

# myresult = mycursor1.fetchall()
# # print(mycursor)
# # print(myresult)
# # print(myresult[1])
# # INSERT INTO `DGHV`.`IoT.Input.SinghaS1.17_20000`(`id`, `soil1`, `soil2`, `bat`, `dataTime`) VALUES ('1', 1, 1, 1, '1')
# query2 = "INSERT INTO `DGHV`.`IoT.Input.SinghaS1.17_80000`(`id`, `soil1`, `soil2`, `bat`, `dataTime`) VALUES  "
# queryValue = ""
# arrM = []
# j = 0
# countx = 1

# for x in myresult:
#     # c = p*q + power(2,l) *r +m    
#     i = 0 
#     while i < len(x) :
#         print(len(x))
#         # print(type(x[i]))
#         if x[i] == "" or x[i] is None :
#             x[i] = ""
#         if type(x[i]) == int or type(x[i]) == float  :
#             if type(x[i]) == float  : 
#                 m = math.ceil(x[i]) *1000
#             else : 
#                 m = x[i] * 1000
            
            
#             c = p * q + power(2,l) * r + m
            
#             d = (c % p) % power(2,l)
#             arrM.append(Decimal(c))            
#             print( str(countx) + "==== " + str(i) + "====" +str(m) +" : "+ str(d) + " : " + str(c))
#         else : 
#             arrM.append(x[i])
        
#         i = i + 1
#     txt = "('{}', {},{},{}, '{}')"   
#     txt = txt.format(str(arrM[0]),str(arrM[1]),str(arrM[2]),str(arrM[3]),str(arrM[4]))
#     print(txt)
#     queryValue = queryValue + txt
#     if j < len(myresult) -1 :
#         queryValue =  queryValue + " , " 
#     txt = ""
#     arrM = []
#     # print(queryValue)
#     j=j+1
#     countx = countx + 1
# query2 = query2 + queryValue 


# mycursor1 = mydb.cursor()


# mycursor1.execute(query2)

# mydb.commit()

# print(mycursor1.rowcount, "record inserted.")

# 81000000000009467427
# 1620000000000189916540
# 1620000000000189703540
# 1620000000000189480540


# 99000000000000000000000000000000000004635937362565283492804310587