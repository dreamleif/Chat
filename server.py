from config import *
import socket
import select
class Server:
    '''
    服务器
    '''
    def __init__(self,ip_port):
        self.ip_port,(self.ip,self.port) = ip_port,ip_port
        self.srvsock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        self.srvsock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.srvsock.bind(self.ip_port)
        self.srvsock.listen( 5 )
        self.descriptors = [self.srvsock]

    def accept_new_connection( self ):
        # 创建新的连接
        newsock, (remhost, remport) = self.srvsock.accept()
        # 将conn对象加入描述符对象列表
        self.descriptors.append( newsock )
    
    def run( self ):
        '''
        客户端启动接口
        '''
        while 1:
            # 监听队列
            (sread, swrite, sexc) = select.select( self.descriptors, [], [] )
            
            # 遍历所有读事件
            for sock in sread:
                if sock == self.srvsock:
                    self.accept_new_connection()
                else:
                    mess = sock.recv(4)
                    # 退出
                    if mess == '':
                        do_quit()
                    else:
                        length = int(mess)
                        if length == 0:
                            do_file()
                        else:
                            mess = sock.recv(length)
                            self.do_request(mess)
    def do_request(self):
        message = eval(mess)
        if message["type"] == REGISTER:
            handle = Register(user)
        if message["type"] == LOG_IN:
            handle = Log_in(user)
        if message["type"] == CHAT:
            handle = CHAT(user,message)
        handle.server_handle()

if __name__ == "__main__":
    server = Server(ip_port)
    server.run()
