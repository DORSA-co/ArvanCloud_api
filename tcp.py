
import socket, pickle




class cloud:
    def __init__(self):
        self.ACCESS_KEY = '2159c713-f554-49d4-b0b5-c5025665fe18'
        self.SECRET_KEY = '0e816c03cf097c12b9a0327db853d41b7f194e21bc3681de265e76ba607c66e3'
        self.host = 'https://s3.ir-thr-at1.arvanstorage.com'


class ProcessData:
    process_id = 0
    project_id = 0
    task_id = 0
    start_time = 0
    end_time = 0
    user_id = 0
    weekend_id = 0
class User:
    def _init_(self, password, username):
        self.password = password
        self.username = username
def connection(obj):
    HOST = '192.168.1.11'
    PORT = 5000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    #s.bind((HOST, PORT))
   # s.listen(1)
    # conn, addr = s.accept()
    # print ('Connected by', addr)

    # data = conn.recv(4096)
    # data_variable = pickle.loads(data)

    # print (data_variable.username)
    # # Access the information by doing data_variable.process_id or data_variable.task_id etc..,
    # print ('Data received from client')

    var=(b'')
    send=pickle.dumps(var)
    s.send(send)
    print('send username & password OK')
#     var=(b'asdasd')
#    # send=pickle.dumps(var)
#     s.send(var)
#     print('send password OK')

    # conn.close()

#connection(username='mialds',password='sadasd')

print('ASDQWD')