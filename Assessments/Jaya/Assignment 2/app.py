from flask import Flask,render_template,request,session
import ibm_db
from DB2 import connection
app = Flask(__name__)

app.secret_key = 'a'


@app.route("/")
def login():
    return render_template('login.html')

@app.route('/loginpage',methods=['GET', 'POST'])
def loginpage():
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32733;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=ftx13630;PWD=l4wr4Z1nGI19hj7a;", '', '')
    print("Connected to DB")
    global userid
    msg = ''

    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        sql = "SELECT * FROM verification WHERE username =? AND password=?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print (account)
        if account:
            session['loggedin'] = True
            session['id'] = account['USERNAME']
            userid=  account['USERNAME']
            session['username'] = account['USERNAME']
            msg = 'Logged in successfully !'
            
            return render_template('welcome.html')
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

@app.route("/register")
def register():
    return render_template('register.html')
    

@app.route("/signup", methods = ['POST'])
def verify_register():
    username = request.form['username']
    email = request.form['email']
    mobile = request.form['mobile']
    password = request.form['password']
    connection.insertvalues1(username,email,mobile,password)
    return render_template("/login")




if __name__ == '__main__':
    app.run(debug=True)