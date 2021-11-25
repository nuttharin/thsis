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
w 

mycursor = mydb.cursor()
# query = "SELECT * FROM `DGHV`.`austin_weather` LIMIT 0,100"
query = "SELECT * FROM `WHO-COVID-19-global-data` LIMIT 40001,60000"
# query = "SELECT * FROM `WHO-COVID-19-global-data`"

mycursor.execute(query)

myresult = mycursor.fetchall()
# print(mycursor)
# print(myresult)
# print(myresult[1])
# INSERT INTO `DGHV`.`austin_weather_enc`(`Date`, `TempHighF`, `TempAvgF`, `TempLowF`, `DewPointHighF`, `DewPointAvgF`, `DewPointLowF`, `HumidityHighPercent`, `HumidityAvgPercent`, `HumidityLowPercent`, `SeaLevelPressureHighInches`, `SeaLevelPressureAvgInches`, `SeaLevelPressureLowInches`, `VisibilityHighMiles`, `VisibilityAvgMiles`, `VisibilityLowMiles`, `WindHighMPH`, `WindAvgMPH`, `WindGustMPH`, `PrecipitationSumInches`) VALUES ('1', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
query2 = "INSERT INTO `DGHV`.`WHO-COVID-19_enc_60000`(`Date_reported`, `Country_code`, `Country`, `WHO_region`, `New_cases`, `Cumulative_cases`, `New_deaths`, `Cumulative_deaths`) VALUES  "
queryValue = ""
arrM = []
j = 0
for x in myresult:
    # c = p*q + power(2,l) *r +m
    i = 4
    
    arrM.append(x[0])
    arrM.append(x[1])
    arrM.append(x[2])
    arrM.append(x[3])
    while i < len(x) :
        # print(len(x))
        # print(type(x[i]))
        if x[i] == "" or x[i] is None :
            x[i] = 0
        if type(x[i]) == int or type(x[i]) == float  :
            if type(x[i]) == float  : 
                m = math.ceil(x[i]) *1000
            else : 
                m = x[i] * 1000
            
            
            c = p * q + power(2,l) * r + m
            
            d = (c % p) % power(2,l)
            arrM.append(Decimal(c))            
            print(str(i) + "====" +str(m) +" : "+ str(d) + " : " + str(c))
        
        i = i + 1
    txt = "('{}', '{}', '{}', '{}', {}, {}, {}, {})"   
    txt = txt.format(str(arrM[0]),str(arrM[1]),str(arrM[2]),str(arrM[3]),str(arrM[4]),str(arrM[5]),str(arrM[6]),str(arrM[7]))
    queryValue = queryValue + txt
    if j < len(myresult) -1 :
        queryValue =  queryValue + " , " 
    txt = ""
    arrM = []
    # print(queryValue)
    j=j+1
query2 = query2 + queryValue 


mycursor = mydb.cursor()


mycursor.execute(query2)

mydb.commit()

print(mycursor.rowcount, "record inserted.")



# 81000000000009467427
# 1620000000000189916540
# 1620000000000189703540
# 1620000000000189480540


99000000000000000000000000000000000004635937362565283492804310587