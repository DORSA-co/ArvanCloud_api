import socket
import pickle





#5.219.148.91
HOST = '192.168.1.11'  # The server's hostname or IP address
PORT = 5000        # The port used by the server

class User:
    def __init__(self, username, password):
        self.password = password
        self.username = username

class Cloud:
    def _init_(self,access_key, secret_key, host, access_bucket):
        self.access_key = access_key
        self.secret_key = secret_key
        self.host = host
        self.access_bucket = access_bucket
        

class tcpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.obj = ''

    
    def login(self, user):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                import cv2
                cv2.waitKey(10)
                
                s.settimeout(0.5)
                print('asdwqd')
                s.connect((self.host, self.port))
                print('connect')
                print(s.connect)
                
                str_ = pickle.dumps(user)
                s.send(str_)
                data = s.recv(1024)
                data=pickle.loads(data)
                print(data)
                print(data.access_key)
                print('asdwqd')
                return(data)
        except:
            return False
            print('exit')
            
           # return False
           # self.obj = pickle.loads(data)

# user = User('amir','1234')
# tcp_client= tcpClient(HOST, PORT)
# tcp_client.login(user)

