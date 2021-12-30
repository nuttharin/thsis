from flask import Flask , jsonify , request
from decimal import Decimal
import psutil
import os


# from flask_restful import Api
import time
import mysql.connector

# connect database MySql
mydb = mysql.connector.connect(
    host="158.108.207.221",
    user="admin1",
    password="51451340",
    database="DGHV"
)

def power(base, exponent):
    # Base Case
    if exponent == 0 :
        return 1
    
    # Recursive Case
    else :
        return base * power(base, exponent - 1)

p = 1000000000000000000000000000000000000000000000000000000000000001

l = 64
q= 99
r= 251314668
powerInt = power(2,l)

maxint = p * q + power(2,l) * r + 9223372036854775807




app = Flask(__name__)
# cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
# cache.init_app(app)

# cache.init_app(app)



@app.route("/test" , methods = ['GET'])
def testX():
    start = time.time()

    print("api => machine/command/get/statusCommand/gasOut") 
    # x =  [0,0,0,0,0,0,0,0,0,0,1]
    # print(x[10])
    time.sleep(2.4)

    # checkLoop = True

    diff = time.time() - start
    strd = '__EXECUTION_TIME__' + str(diff)
        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd ,
        "data" : str(myresult)
    })  

@app.route("/get/enc/all" , methods = ['GET'])
def getallsimple20000():
    start = time.time()
    rows = request.args.get('rows')
    print(rows)
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `IoT.Input.SinghaS1.17_"+str(rows)+"`")

    myresult = mycursor.fetchall()
    diff = time.time() - start
    strd =  str(diff)
    # print(myresult)
        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd 
        # "data" : str(myresult)

    })  

@app.route("/get/simple/all" , methods = ['GET'])
def getallraw20000():
    start = time.time()

    mycursor = mydb.cursor()
    rows = request.args.get('rows')
    print(rows)
    mycursor.execute("SELECT * FROM `IoT.Input.SinghaS1.17_raw_"+str(rows)+"`")

    myresult = mycursor.fetchall()
    diff = time.time() - start
    strd =  str(diff)
    # cache.clear()
        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd 
        # ,"data" :str(myresult)
    })  

@app.route("/get/dghv/all" , methods = ['GET'])
def getalldghv20000():
    i = 0
    while i < 5 :
        start = time.time()

        mycursor = mydb.cursor()
        rows = request.args.get('rows')
        print(rows)
        mycursor.execute("SELECT * FROM `IoT.Input.SinghaS1.17_dghv_"+str(rows)+"`")
        myresult = mycursor.fetchall()
        print(len(myresult))
        diff = time.time() - start
        strd =  str(diff)
        print(strd)
        i=i+1
        # cache.clear()
        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd 
        # ,"data" :str(myresult)
    })  

@app.route("/get/dghv/all" , methods = ['GET'])
def getallencDGHV():
    start = time.time()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `IoT.Input.SinghaS1.17_dghv_"+str(rows)+"`")

    myresult = mycursor.fetchall()
    diff = time.time() - start
    strd =  str(diff)

        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd 
        # ,"data" : str(myresult)
    })  

# ================= MAX ======================================
@app.route("/get/enc/all/max" , methods = ['GET'])
def getallsimple20000max():
    start = time.time()
    rows = request.args.get('rows')
    print(rows)
    mycursor = mydb.cursor()

    mycursor.execute("SELECT MAX(soil1) as maxv FROM `IoT.Input.SinghaS1.17_"+str(rows)+"`")

    myresult = mycursor.fetchone()
    print(myresult[0])

    d = ((myresult[0] % p) % power(2,l))/1000
    diff = time.time() - start
    strd =  diff
    print(d)
      
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd 
        # "data" : str(myresult)

    })  

@app.route("/get/simple/all/max" , methods = ['GET'])
def getallraw20000max():
    start = time.time()

    mycursor = mydb.cursor()
    rows = request.args.get('rows')
    print(rows)
    mycursor.execute("SELECT MAX(soil1) as maxv FROM `IoT.Input.SinghaS1.17_raw_"+str(rows)+"`")

    myresult = mycursor.fetchone()
    print(myresult)

    diff = time.time() - start
    strd =  diff
    # cache.clear()
        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd 
        # ,"data" :str(myresult)
    })  
# ============================================================

# ================= MIN ======================================
@app.route("/get/enc/all/min" , methods = ['GET'])
def getallsimple20000min():
    start = time.time()
    rows = request.args.get('rows')
    print(rows)
    mycursor = mydb.cursor()

    mycursor.execute("SELECT MIN(soil1) as maxv FROM `IoT.Input.SinghaS1.17_"+str(rows)+"`")

    myresult = mycursor.fetchone()
    print(myresult[0])

    d = ((myresult[0] % p) % power(2,l))/1000
    diff = time.time() - start
    strd =  diff
    print(d)
      
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd 
        # "data" : str(myresult)

    })  

@app.route("/get/simple/all/min" , methods = ['GET'])
def getallraw20000min():
    start = time.time()

    mycursor = mydb.cursor()
    rows = request.args.get('rows')
    print(rows)
    mycursor.execute("SELECT MIN(soil1) as maxv FROM `IoT.Input.SinghaS1.17_raw_"+str(rows)+"`")

    myresult = mycursor.fetchone()
    print(myresult)

    diff = time.time() - start
    strd =  diff
    # cache.clear()
        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd 
        # ,"data" :str(myresult)
    })  
# ============================================================

# ================= SUM ======================================
@app.route("/get/enc/all/sum" , methods = ['GET'])
def getallsimple20000sum():
    i = 0
    while i < 5:
        mysum = 0
        mysumEnc = 0
        xx = 0
        start = time.time()
        rows = request.args.get('rows')
        print(rows)
        mycursor = mydb.cursor()

        mycursor.execute("SELECT soil1 FROM `IoT.Input.SinghaS1.17_"+str(rows)+"`")

        myresult = mycursor.fetchall()
        # cMaxint = p * q + power(2,l) * r + mMaxint
        # temp = math.floor(c/cMaxint) 
        # print((c-(temp*cMaxint)) % p % power(2,l) + ((temp*mMaxint)))
        # print(myresult[0])
        # print((( myresult[0] % p) % power(2,l))/1000 )
        # print(len(myresult))
        for row in myresult:
            # print(row[0])
            d = ((row[0] % p) % powerInt)/1000
            # print(d)
            mysum = mysum + d
             
            mysumEnc = mysumEnc + Decimal(row[0])
            if mysumEnc > maxint :
                xx = xx + ((mysumEnc % p) % powerInt)/1000
                mysumEnc = 0
            print(xx)

        print("--------")
        print(xx)
        # print(len(str(mysumEnc)))
        # print(((mysumEnc % p) % powerInt)/1000)
        mycursor.close()
        
        diff = time.time() - start
        strd =  diff
        print(strd)
        i = i+1
    # print(mysum)
    # print("=====")
    # print(len(mysumEnc))
    # print(((mysumEnc % p) % power(2,l))/1000)
      
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd 
        # "data" : str(myresult)

    })  

@app.route("/get/dghv/all/sum" , methods = ['GET'])
def getalldghv20000sum():
    i = 0
    while i < 5:
        mysum = 0
        mysumEnc = 0
        xx = 0
        integer_sum = 0
        start = time.time()
        rows = request.args.get('rows')
        print(rows)
        mycursor = mydb.cursor()

        mycursor.execute("SELECT soil1 FROM `IoT.Input.SinghaS1.17_"+str(rows)+"`")

        myresult = mycursor.fetchall()
        # cMaxint = p * q + power(2,l) * r + mMaxint
        # temp = math.floor(c/cMaxint) 
        # print((c-(temp*cMaxint)) % p % power(2,l) + ((temp*mMaxint)))
        # print(myresult[0])
        # print((( myresult[0] % p) % power(2,l))/1000 )
        # print(len(myresult))
        for row in myresult:
            # print(row[0])
            d = ((row[0] % p) % powerInt)/1000
            # print(d)
            mysum = mysum + d
             
            integer_sum = int(bin(integer_sum), 2) + int(row[0], 2)
            binary_sum = bin(integer_sum)
            print(binary_sum)

        print("--------")
        print(xx)
        # print(len(str(mysumEnc)))
        # print(((mysumEnc % p) % powerInt)/1000)
        mycursor.close()
        
        diff = time.time() - start
        strd =  diff
        print(strd)
        i = i+1
    # print(mysum)
    # print("=====")
    # print(len(mysumEnc))
    # print(((mysumEnc % p) % power(2,l))/1000)
      
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd 
        # "data" : str(myresult)

    })  

@app.route("/get/simple/all/sum" , methods = ['GET'])
def getallraw20000sum():
    start = time.time()

    mycursor = mydb.cursor()
    rows = request.args.get('rows')
    print(rows)
    mycursor.execute("SELECT SUM(soil1) as maxv FROM `IoT.Input.SinghaS1.17_raw_"+str(rows)+"`")

    myresult = mycursor.fetchall()
    print(myresult)
    

    diff = time.time() - start
    strd =  diff
    # cache.clear()
        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd 
        # ,"data" :str(myresult)
    })
 
# ============================================================

# ================= AVG ======================================
@app.route("/get/enc/all/avg" , methods = ['GET'])
def getallsimple20000avg():
    i = 0
    while i<5 :
        mysum = 0
        mysumEnc = 0
        mysumEncDe = 0
        start = time.time()
        rows = request.args.get('rows')
        print(rows)
        mycursor = mydb.cursor()

        mycursor.execute("SELECT soil1 FROM `IoT.Input.SinghaS1.17_"+str(rows)+"`")

        myresult = mycursor.fetchall()
        # cMaxint = p * q + power(2,l) * r + mMaxint
        # temp = math.floor(c/cMaxint) 
        # print((c-(temp*cMaxint)) % p % power(2,l) + ((temp*mMaxint)))
        # print(myresult[0])
        # print((( myresult[0] % p) % power(2,l))/1000 
        x = 0
        for row in myresult:
            print(row[0])
            d = ((row[0] % p) % power(2,l))/1000
            # print(d)
            mysum = mysum + d
            mysumEnc = mysumEnc + row[0]
            print(Decimal(row[0]))
            x = x + 1
            # if x%10 == 0 : 
            #     mysumEncDe = mysumEncDe + ((mysumEnc % p) % power(2,l))/1000
            #     mysumEnc = 0
        diff = time.time() - start
        strd =  diff
        print(strd)
        mycursor.close()
        
       
        i = i + 1
    d = ((mysumEnc % p) % power(2,l))/1000
    print(d)
    # print("=====")
    # print(len(mysumEnc))
    # print(((mysumEnc % p) % power(2,l))/1000)
      
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd 
        # "data" : str(myresult)

    })  

@app.route("/get/simple/all/avg" , methods = ['GET'])
def getallraw20000avg():
    i = 0
    while i<1 :
        start = time.time()

        mycursor = mydb.cursor()
        rows = request.args.get('rows')
        print(rows)
        mycursor.execute("SELECT AVG(soil1) as maxv FROM `IoT.Input.SinghaS1.17_raw_"+str(rows)+"`")

        myresult = mycursor.fetchone()
        # print(myresult[0])

        diff = time.time() - start
        strd =  diff
        # print(strd)
        mycursor.close()
        i = i + 1

        print("ram")
        # cache.clear()
        print(psutil.cpu_percent())
        # gives an object with many fields
        psutil.virtual_memory()
        # you can convert that object to a dictionary 
        # print(dict(psutil.virtual_memory()._asdict()))
        # you can have the percentage of used RAM
        # print(psutil.virtual_memory().percent)
        # 79.2
        # you can calculate percentage of available memory
        print("ram %")
        print(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
        print("total")
        print(psutil.virtual_memory().total)
        print(psutil.virtual_memory().available)
        # 20.8

        print(psutil.cpu_percent())
        print(psutil.virtual_memory())  # physical memory usage
        print('memory % used:', psutil.virtual_memory()[2])
        print("============================")
        process = psutil.Process(os.getpid())
        print(process.memory_info().rss)  # in bytes 

        i = i + 1
            
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd 
        # ,"data" :str(myresult)
    })
 
# ============================================================
if __name__ == "__main__":
    app.run(host= "10.0.0.3" ,debug=True , port=5000)
    # app.run(host="192.168.0.103" ,debug=True , port=5000)

    # app.run(debug=True , port=5000)
print("start")