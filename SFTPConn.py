import pysftp

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
        self.Show()
        srv = pysftp.Connection(host=self.hostname,username=self.username, password=self.password)
        print("OUT connection")
        return srv

    def BrowseDir(self,srv, path):
        data = srv.listdir(remotepath=path)

        print(data)
        return data



# c = SFTPConnection('OBLIVION', 'hp', 'Sumedh11!',22)
# srv=c.Connect
# c.BrowseDir(srv,"G:/")
