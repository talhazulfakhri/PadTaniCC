from unittest import result
from flask import Flask, request
from flask_mysqldb import MySQL
from flask import jsonify
import yaml

app = Flask(__name__)

db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/padi', methods=['GET'])
def padi():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM padis")
    if result > 0:
        varietas = cur.fetchall()
        return jsonify({'data': varietas}, 200)
  

@app.route('/pupuk', methods=['GET'])
def pupuk():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM pupuks")
    if result > 0:
        varietas = cur.fetchall()
        return jsonify({'data': varietas}, 200)

@app.route('/register', methods=['POST'])
def register():
        user = request.form
        name = user['name']
        email = user['email']
        password = user['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tbl_user(name, email, password) VALUES(%s, %s, %s)",(name, email, password))
        mysql.connection.commit()
        cur.close()
        return jsonify({'data': user}, 200)

if __name__ == '__main__':
    app.run(debug=True)