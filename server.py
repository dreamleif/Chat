from config import *
import socket
import select
from register import *
from log_in import *
class Server:
    '''
    服务器
    '''
    def __init__(self,ip_port):
        self.ip_port,(self.ip,self.port) = ip_port,ip_port
        self.srvsock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        self.srvsock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.srvsock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
        self.srvsock.bind(self.ip_port)
        self.srvsock.listen( 5 )
        self.descriptors = [self.srvsock]

    def accept_new_connection(self):
        # 创建新的连接
        newsock, (remhost, remport) = self.srvsock.accept()
        # 将conn对象加入描述符对象列表
        self.descriptors.append(newsock)
    
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
                    mess = sock.recv(4).decode()
                    print(mess)
                    # 退出
                    if mess == '':
                        # do_quit()
                        pass
                    else:
                        length = int(mess)
                        if length == 0:
                            do_file()
                        else:
                            mess = sock.recv(length)
                            self.do_request(mess,sock)
    def do_request(self,mess,conn):
        #　处理请求
        mess = eval(mess)
        if mess["type"] == REGISTER:
            handle = RegisterServer(mess,conn)
        if mess["type"] == LOG_IN:
            handle = Log_inServer(mess,conn)
        if mess["type"] == CREATROOM:
            handle = CreatroomServer(mess,conn)
        if mess["type"] == ENTERROOM:
            handle = EnterroomServer(mess,conn)
        if mess["type"] == CHAT:
            handle = ChatServer(mess,conn)
        if mess["type"] == EXITROOM:
            handle = ExitroomServer(mess,conn)
        if mess["type"] == EXIT:
            handle = ExitServer(mess,conn)
        handle.server_handle()

if __name__ == "__main__": 
    server = Server(ip_port)
    server.run()
