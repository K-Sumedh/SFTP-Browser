import pysftp
import os

global server
global SrvObj

class SFTPConnection:
    def __init__(self,hostname, username, password,port):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port
        print('Username :',self.username, 'Hostname :', self.hostname, 'Password :',self.password, 'Port :',self.port)
        print(self)

    def Show(self):
        print('Username : ',self.username, 'Hostname : ', self.hostname, 'Password : ',self.password, 'Port : ',self.port)

    def Connect(self):
        print("In connection")
        #self.Show()
        srv = pysftp.Connection(host=self.hostname,username=self.username, password=self.password)
        print("OUT connection")
        return srv

    def BrowseDir(self,srv, path):
        dataDict = {}
        data = srv.listdir(remotepath=path)
        for items in data:
            #if srv.isdir(os.path.join(path, items)):
            if srv.isdir(path+"/"+items):
                dataDict[items] = True
            else:
                dataDict[items] = False
        print('DataDict : ',dataDict)
        return dataDict



# SrvObj = SFTPConnection('OBLIVION', 'hp', 'Sumedh11!',22)
# server=SrvObj.Connect()
# SrvObj.BrowseDir(server,"C:")
