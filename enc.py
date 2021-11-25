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
q=99
r=5

 

mycursor = mydb.cursor()
# query = "SELECT * FROM `DGHV`.`austin_weather` LIMIT 0,100"
query = "SELECT * FROM `DGHV`.`austin_weather_test_10000`"
mycursor.execute(query)

myresult = mycursor.fetchall()
# print(mycursor)
print(myresult)
# print(myresult[1])
# INSERT INTO `DGHV`.`austin_weather_enc`(`Date`, `TempHighF`, `TempAvgF`, `TempLowF`, `DewPointHighF`, `DewPointAvgF`, `DewPointLowF`, `HumidityHighPercent`, `HumidityAvgPercent`, `HumidityLowPercent`, `SeaLevelPressureHighInches`, `SeaLevelPressureAvgInches`, `SeaLevelPressureLowInches`, `VisibilityHighMiles`, `VisibilityAvgMiles`, `VisibilityLowMiles`, `WindHighMPH`, `WindAvgMPH`, `WindGustMPH`, `PrecipitationSumInches`) VALUES ('1', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
query2 = "INSERT INTO `DGHV`.`austin_weather_enc_10000`(`TempHighF`, `TempAvgF`, `TempLowF`, `DewPointHighF`, `DewPointAvgF`, `DewPointLowF`, `HumidityHighPercent`, `HumidityAvgPercent`, `HumidityLowPercent`, `SeaLevelPressureHighInches`, `SeaLevelPressureAvgInches`, `SeaLevelPressureLowInches`, `VisibilityHighMiles`, `VisibilityAvgMiles`, `VisibilityLowMiles`, `WindHighMPH`, `WindAvgMPH`, `WindGustMPH`, `PrecipitationSumInches`) VALUES "
queryValue = ""
arrM = []
j = 0
for x in myresult:
    # c = p*q + power(2,l) *r +m
    i = 0 
    # print(len(myresult))
    while i < len(x) :
        # print(len(x))
        # print(type(x[i]))
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
    # print(arrM)
    txt = "({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}) "   
    txt = txt.format(str(arrM[0]),str(arrM[1]),str(arrM[2]),str(arrM[3]),str(arrM[4]),str(arrM[5]),str(arrM[6]),str(arrM[7]),str(arrM[8]),str(arrM[9]),str(arrM[10]),str(arrM[11]),str(arrM[12]),str(arrM[13]),str(arrM[14]),str(arrM[15]),str(arrM[16]),str(arrM[17]),str(arrM[18]))
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