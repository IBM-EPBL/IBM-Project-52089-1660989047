from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html')


@app.route("/register")
def register():
    return render_template('register.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if(__name__) == '__main__':
    app.run(debug=True)