from config import *
import socket
import sys
sys.path.append("./dao/")
from table import *
from register import *
from log_in import *
class Client:
    '''
    客户端
    '''
    def __init__(self,ip_port):
        self.ip_port,(self.ip,self.port) = ip_port,ip_port
        self.clisocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clisocket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    def run(self):
        '''
        客户端启动
        '''
        try:
            self.clisocket.connect(self.ip_port)
            print('ok')
        except Exception as e:
            print('connect fail %s'%e)
        

    def log_in(self,user_id,user_password):
        '''
        登录
        '''
        user = User(user_id,user_password,None,None,None)
        handle = Log_inClient(self.clisocket,user)
        handle.request()
        resp = handle.response()
        return resp.decode()
    
    def register(self,user_id,user_name,user_password,user_email,user_phone_number):
        '''
        注册
        '''
        user = User(user_id,user_name,user_password,user_email,user_phone_number)
        # print(user)
        handle = RegisterClient(self.clisocket,user)
        handle.request()
        resp = handle.response()
        return resp.decode()

    def enterroom(self,room_number):
        
    def createroom(self,room_theme,room_info):
        '''
        创建房间
        '''
        
    def chat(self,message):
    
    def exitroom(self):

    def exit():


if __name__== "__main__":
    client = Client(ip_port)
    client.run()
    # resp = client.register("123","leif","123456","312@312.com",'1241432342')
    resp = client.log_in("123","123456")
    print(resp)
