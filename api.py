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





app = Flask(__name__)

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
        "time" : strd ,
        "data" : str(myresult)

    })  

@app.route("/get/enc/all/40000" , methods = ['GET'])
def getallsimple40000():
    start = time.time()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `IoT.Input.SinghaS1.17_20000`")

    myresult = mycursor.fetchall()
    diff = time.time() - start
    strd =  str(diff)
    # print(myresult)
        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd ,
        "data" : str(myresult)

    })

@app.route("/get/enc/all/60000" , methods = ['GET'])
def getallsimple60000():
    start = time.time()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `IoT.Input.SinghaS1.17_20000`")

    myresult = mycursor.fetchall()
    diff = time.time() - start
    strd =  str(diff)
    # print(myresult)
        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd ,
        "data" : str(myresult)

    })

@app.route("/get/enc/all/80000" , methods = ['GET'])
def getallsimple80000():
    start = time.time()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `IoT.Input.SinghaS1.17_20000`")

    myresult = mycursor.fetchall()
    diff = time.time() - start
    strd =  str(diff)
    # print(myresult)
        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd ,
        "data" : str(myresult)

    })

@app.route("/get/enc/all/100000" , methods = ['GET'])
def getallsimple100000():
    start = time.time()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `IoT.Input.SinghaS1.17_20000`")

    myresult = mycursor.fetchall()
    diff = time.time() - start
    strd =  str(diff)
    # print(myresult)
        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd ,
        "data" : str(myresult)

    })

@app.route("/get/enc/all/120000" , methods = ['GET'])
def getallsimple120000():
    start = time.time()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `IoT.Input.SinghaS1.17_20000`")

    myresult = mycursor.fetchall()
    diff = time.time() - start
    strd =  str(diff)
    # print(myresult)
        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd ,
        "data" : str(myresult)

    })

@app.route("/get/enc/all/140000" , methods = ['GET'])
def getallsimple140000():
    start = time.time()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `IoT.Input.SinghaS1.17_20000`")

    myresult = mycursor.fetchall()
    diff = time.time() - start
    strd =  str(diff)
    # print(myresult)
        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd ,
        "data" : str(myresult)

    })

@app.route("/get/enc/all/160000" , methods = ['GET'])
def getallsimple160000():
    start = time.time()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `IoT.Input.SinghaS1.17_20000`")

    myresult = mycursor.fetchall()
    diff = time.time() - start
    strd =  str(diff)
    # print(myresult)
        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd ,
        "data" : str(myresult)

    })

@app.route("/get/enc/all/180000" , methods = ['GET'])
def getallsimple180000():
    start = time.time()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `IoT.Input.SinghaS1.17_20000`")

    myresult = mycursor.fetchall()
    diff = time.time() - start
    strd =  str(diff)
    # print(myresult)
        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd ,
        "data" : str(myresult)

    })

@app.route("/get/enc/all/200000" , methods = ['GET'])
def getallsimple200000():
    start = time.time()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `IoT.Input.SinghaS1.17_20000`")

    myresult = mycursor.fetchall()
    diff = time.time() - start
    strd =  str(diff)
    # print(myresult)
        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd ,
        "data" : str(myresult)

    })


@app.route("/get/simple/all/20000" , methods = ['GET'])
def getallenc20000():
    start = time.time()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `IoT.Input.SinghaS1.17_raw_20000`")

    myresult = mycursor.fetchall()
    diff = time.time() - start
    strd =  str(diff)

        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd ,
        "data" :str(myresult)
    })  



@app.route("/get/dghv/all" , methods = ['GET'])
def getallencDGHV():
    start = time.time()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `IoT.Input.SinghaS1.17_dghv_20000`")

    myresult = mycursor.fetchall()
    diff = time.time() - start
    strd = '__EXECUTION_TIME__' + str(diff)

        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd ,
        "data" : str(myresult)
    })  




if __name__ == "__main__":
    app.run(host= "10.0.0.3" ,debug=True , port=5000)
    #app.run(host="192.168.250.12" ,debug=True , port=5000)

    # app.run(debug=True , port=5000)
print("start")