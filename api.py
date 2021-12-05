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

        
    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "time" : strd 
        ,"data" :str(myresult)
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