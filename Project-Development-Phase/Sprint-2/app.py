from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from flask import Flask, render_template, request
from newsapi import NewsApiClient

serviceUsername = ""
servicePassword = ""
serviceURL = ""

client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()

app = Flask(__name__)


def addNewUser(userName,userEmail,userPassword):
    jsondata = {}
    jsondata["userName"] = str(userName)
    jsondata["userEmail"] = str(userEmail)
    jsondata["userPassword"] = str(userPassword)

    myDataBase = client['database1']
    newDocument = myDataBase.create_document(jsondata)


def authenticate(userName,userEmail):
    myDataBase = client['database1']
    result_collection = Result(myDataBase.all_docs, include_docs=True)
    for data in result_collection:

        if data['doc']['userName'] == str(userName):
            return True
        if data['doc']['userEmail'] == str(userEmail):
            return True
    return False

def authenticateLogin(userEmail,userPassword):
    myDataBase = client['database1']
    result_collection = Result(myDataBase.all_docs, include_docs=True)
   
    for data in result_collection:
        if data['doc']['userPassword'] == str(userPassword) and data['doc']['userEmail'] == str(userEmail):    
            return True
    return False

@app.route("/login",methods = ['POST', 'GET'])
def loginUser():
    
    userEmail = request.form.get("email")
    userPassword = request.form.get("pswd")


    if(authenticateLogin(userEmail,userPassword)):
        return news()
    return render_template("index.html")

@app.route("/register",methods = ['POST', 'GET'])
def registerUserData():
    userName = request.form.get("un")
    userEmail = request.form.get("ue")
    userPassword = request.form.get("up")
    
    print(userEmail,userName,userPassword)
    if(authenticate(userName=userName,userEmail=userEmail)):
        return render_template("index.html")
    addNewUser(userName,userEmail,userPassword)
    return news()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def hh():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)