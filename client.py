from config import *
import socket

class Client:
    '''
    客户端
    '''
    def __init__(self,ip_port):
        self.ip_port,(self.ip,self.port) = ip_port,ip_port
        self.clisocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clisocket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    def run(self):
        try:
            self.clisocket.connect(self.ip_port)
            print('ok')
        except Exception as e:
            print('connect fail %s'%e)
        

    def log_in(self):
        log_in
    
    def register(self,user):
        handle = Register(user)
        handle.client_sent(R)
    def start(self):
        pass

if __name__== "__main__":
    client = Client(ip_port)
    client.run()
