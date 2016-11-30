from flask import Flask, request,jsonify
from flaskext.mysql import MySQL
from flask_restful import reqparse

from random import randrange

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'user'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
 
@app.route("/")
def hello():
    return "Test Flask app"

@app.route("/Authenticate")
def Authenticate():
    username = request.args.get("username")
    password = request.args.get("password")
    if username is None:
        return "Please enter valid Username"
    elif password  is None:
        return "Please enter valid passowrd"
    
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from User where userName like BINARY '" + username + "' and password like BINARY '" + password + "'")
    data = cursor.fetchone()
    print data
    if data is None:
        return "Username or password is incorrect"
    else:
        return "Login successful"

@app.route("/random")
def random():
    start=request.args.get("start",type=int)
    end=request.args.get("end",type=int)
    if start is None:
        return "Please enter valid start number for random number generation within range"
    elif end is None:
        return "Please enter valid end number for random number generation within range"
    return jsonify(randrange(start+end))

    

 
if __name__ == "__main__":
    app.run(debug=True)

