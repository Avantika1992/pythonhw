from flask import Flask,url_for,redirect,render_template,request
app = Flask(__name__)
from datetime import datetime
import os
import mysql.connector

mydb=mysql.connector.connect(host="db.ctnh6xid4c7z.us-east-1.rds.amazonaws.com",user="avantika",passwd="avantika",db="avi")
cur=mydb.cursor()
cur.execute("SELECT * FROM avi.employees where name like \"aira\"")
for i in cur.fetchall():
   c=i[0]
   print(i[0])
cur.close()
mydb.close()

PEOPLE_FOLDER = os.path.join('static', 'photo')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


@app.route('/')
def show_index():
   full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Scr.png')
   return render_template("index.html", user_image = full_filename)

@app.route('/cur')
def curi():
   return c

@app.route('/health')
def health():
   if (mydb):
       return "<h1>Connection successful</h1>"



if __name__ == '__main__':
  app.run(host='0.0.0.0')
