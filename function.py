
class FunctionServer:
    def __init__(self,mess,conn):
        self.mess = mess
        self.conn = conn

        
    def server_handle(self):
        '''
        服务器处理
        '''
        pass

class FunctionClient:
    def __init__(self,clisocket,user = None):
        self.user = user
        self.clisocket = clisocket
   
    def request(self):
        '''
        客户端发送请求
        '''
        pass

    def response(self):
        '''
        客户端接收响应
        '''
        pass

