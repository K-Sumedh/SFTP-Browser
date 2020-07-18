# import pysftp
# import flask
#
# srv = pysftp.Connection(host="OBLIVION", username="hp",
# password="Sumedh11!")
#
#
# # Get the directory and file listing
# srv.chdir("G:\PROJECTS\FTP\Storage")
# data = srv.listdir()
# # Closes the connection
# srv.close()
#
# # Prints out the directories and files, line by line
# for i in data:
#     print (i)
from flask import Flask, render_template, request
import SFTPConn as conn
app = Flask(__name__)

global server
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  print ('I got clicked!')
  return 'Click.'

@app.route('/login/',  methods=['POST'])
def Login():
    uname = request.form['username']
    pwd = request.form['pwd']
    host = request.form['hostname']
    port = request.form['port']
    #print(uname ,pwd, host,port)
    try:
        #conn.SrvObj = conn.SFTPConnection(hostname="OBLIVION",username="hp", password="Sumedh11!", port=22)
        conn.SrvObj = conn.SFTPConnection(hostname=host,username=uname, password=pwd, port=port)
        conn.server = conn.SrvObj.Connect()
        print('logged in successfully',conn.server)
        return render_template('login.html',  message='Login Successfull')
    except :
        print('login unsucessful!')
        return render_template('index.html', message='Login Failed.Try again.')

@app.route('/browse/', methods=['POST'])
def Browse():
    path = request.form['browse']
    print('browse',conn.server)
    data = conn.SrvObj.BrowseDir(conn.server, path)
    return render_template('login.html', list=data)

if __name__ == '__main__':
  app.run(debug=True)
