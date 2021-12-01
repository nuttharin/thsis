from flask import Flask , jsonify , request
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
        "data" : strd
    })  

@app.route("/get/simple/all" , methods = ['GET'])
def getallsimple():
    start = time.time()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `IoT.Input.SinghaS1.17_20000`")

    myresult = mycursor.fetchall()
    diff = time.time() - start
    strd = '__EXECUTION_TIME__' + str(diff)

        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "data" : strd
    })  

@app.route("/get/enc/all" , methods = ['GET'])
def getallenc():
    start = time.time()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `IoT.Input.SinghaS1.17_raw_20000`")

    myresult = mycursor.fetchall()
    diff = time.time() - start
    strd = '__EXECUTION_TIME__' + str(diff)

        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "data" : strd
    })  

@app.route("/get/encDGHV/all" , methods = ['GET'])
def getallencDGHV():
    start = time.time()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `IoT.Input.SinghaS1.17_raw_20000`")

    myresult = mycursor.fetchall()
    diff = time.time() - start
    strd = '__EXECUTION_TIME__' + str(diff)

        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "data" : strd
    })  

if __name__ == "__main__":
    app.run(host= "158.108.207.221" ,debug=True , port=5000)
    #app.run(host="192.168.250.12" ,debug=True , port=5000)

    # app.run(debug=True , port=5000)
print("start")