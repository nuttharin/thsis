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
p = 251312513125131

# l = 64
q= 99
r= 25131





y = 0
maxRows = 40000
while y < maxRows :
    if y == 0 :
        y = 1
        rows = "BETWEEN "+str(y)+" AND "+str(10000)
    else :
        rows = "BETWEEN "+str(y)+" AND "+str(y+10000)

    mycursor = mydb.cursor()
    # query = "SELECT * FROM `DGHV`.`austin_weather` LIMIT 0,100"
    query = "SELECT t2.id , t2.soil1 , t2.soil2 ,t2.bat , t2.dataTime FROM ( SELECT t.*, @rownum := @rownum + 1 AS rn FROM `IoT.Input.SinghaS1.17` as t , (SELECT @rownum := 0) r ) t2 WHERE t2.rn BETWEEN 1 AND 10000"
    # query = "SELECT * FROM `WHO-COVID-19-global-data`"

    mycursor.execute(query)

    myresult = mycursor.fetchall()

    # print(myresult)
    # print(myresult[1])
    # INSERT INTO `DGHV`.`IoT.Input.SinghaS1.17_20000`(`id`, `soil1`, `soil2`, `bat`, `dataTime`) VALUES ('1', 1, 1, 1, '1')
    query2 = "INSERT INTO `DGHV`.`IoT.Input.SinghaS1.17_dghv_original_40000`(`id`, `soil1`, `soil2`, `bat`, `dataTime`) VALUES  "
    queryValue = ""
    arrM = []
    j = 0
    m = ""
    for x in myresult:
        # c = p*q + 2*r + m    
        i = 0 
        print("i=>",j+y)
        while i < len(x) :
            # print(len(x))
            # print(type(x[i]))
            if x[i] == "" or x[i] is None :
                x[i] = ""
            if type(x[i]) == int or type(x[i]) == float  :
                if type(x[i]) == float  : 
                    m = '{0:b}'.format(math.ceil(x[i]*1000))
                else : 
                    m = '{0:b}'.format(x[i] * 1000)
                
                # positive_binary = '{0:b}'.format(m)
                k = 0 
                c = ""
                cipherConnect = ""
                while k < len(m) :
                    cipher1 = q * p + 2 * r + int(m[k]) 
                    cipherConnect = cipherConnect + str(cipher1)
                    if k < len(m) -1 :
                        cipherConnect = cipherConnect +","
                    if k == len(m)-1 : 
                        c = cipherConnect
                    k=k+1

                        
                # print(str(x[i]*1000)+"===="+str(m)+"====")


                # c = p*q + 2*r + m  
                
                arrM.append(c)            
            else : 
                arrM.append(x[i])

            i = i + 1
        

        txt = "('{}', '{}','{}','{}', '{}')"   
        txt = txt.format(str(arrM[0]),str(arrM[1]),str(arrM[2]),str(arrM[3]),str(arrM[4]))

        
        # print(txt)
        queryValue = queryValue + txt
        if j < len(myresult) -1 :
            queryValue =  queryValue + " , " 
        txt = ""
        arrM = []
        # print(queryValue)
        j=j+1


    query2 = query2 + queryValue 
    # print(query2)

    mycursor1 = mydb.cursor()


    mycursor1.execute(query2)

    mydb.commit()

    print(mycursor1.rowcount, "record inserted.")
    y = y +10000

