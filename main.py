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
    try:
        browsePath = request.form['browsePath']
        print('browse',conn.server, "------------",path+'/'+browsePath)
        DirData = conn.SrvObj.BrowseDir(conn.server, path+'/'+browsePath)
        return render_template('browse.html', list=DirData, path=path+'/'+browsePath)
    except:
        DirData = conn.SrvObj.BrowseDir(conn.server, path)
        return render_template('browse.html', list=DirData, path=path)

@app.route('/upload/', methods=['POST'])
def upload():
    fileNameData = request.get_json()
    path = request.form['browse']
    print("AddtoSelectedList : ",fileNameData)
    try:
        browsePath = request.form['browsePath']
        print('browse',conn.server, "------------",path+'/'+browsePath)
        DirData = conn.SrvObj.BrowseDir(conn.server, path+'/'+browsePath)
        return render_template('browse.html', list=DirData, path=path+'/'+browsePath)
    except:
        DirData = conn.SrvObj.BrowseDir(conn.server, path)
        return render_template('browse.html', list=DirData, path=path)


if __name__ == '__main__':
  app.run(debug=True)
