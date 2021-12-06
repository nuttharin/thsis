from flask import Flask , jsonify , request


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



if __name__ == "__main__":
    app.run(host= "10.0.0.3" ,debug=True , port=5000)
    #app.run(host="192.168.250.12" ,debug=True , port=5000)

    # app.run(debug=True , port=5000)
print("start")