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

p=10000000000000000000000000000001   #key

l = 32
q=random.randint(3, 100)
r=random.randint(3, 10)

 

mycursor = mydb.cursor()
query = "SELECT * FROM `WHO-COVID-19-data` LIMIT 0,100"
mycursor.execute(query)

myresult = mycursor.fetchall()
# print(mycursor)
# print(myresult)
# print(myresult[1])
# INSERT INTO `DGHV`.`austin_weather_enc`(`Date`, `TempHighF`, `TempAvgF`, `TempLowF`, `DewPointHighF`, `DewPointAvgF`, `DewPointLowF`, `HumidityHighPercent`, `HumidityAvgPercent`, `HumidityLowPercent`, `SeaLevelPressureHighInches`, `SeaLevelPressureAvgInches`, `SeaLevelPressureLowInches`, `VisibilityHighMiles`, `VisibilityAvgMiles`, `VisibilityLowMiles`, `WindHighMPH`, `WindAvgMPH`, `WindGustMPH`, `PrecipitationSumInches`) VALUES ('1', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
query2 = "INSERT INTO `DGHV`.`WHO-COVID-19-data`(`Country_code`, `New_cases`, `Cumulative_cases`, `New_deaths`, `Cumulative_deaths`) VALUES "
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
                m = math.ceil(x[i]) *11111111
            else : 
                m = x[i] * 11111111
            
            
            c = p * q + power(2,l) * r + m
            d = (c % p) % power(2,l)
            arrM.append(Decimal(c))            
            print(str(m) +" : "+ str(d) + " : " + str(c))
        else :
            arrM.append(x[i]) 
        i = i + 1
    # print(arrM)
    txt = "({}, {}, {}, {}, {}) "   
    txt = txt.format(str(arrM[0]),str(arrM[1]),str(arrM[2]),str(arrM[3]),str(arrM[4]))
    queryValue = queryValue + txt
    if j < len(myresult) -1 :
        queryValue =  queryValue + " , " 
    txt = ""
    arrM = []
    # print(queryValue)
    j=j+1

630000000000000000000034359753431
700000000000000000000021489836550
230000000000000000000035853659926

# query2 = query2 + queryValue 


# mycursor = mydb.cursor()



# mycursor.execute(query2)

# mydb.commit()

print(mycursor.rowcount, "record inserted.")