from config import *
import sys
sys.path.append("./dao")
from table import *
from dao import *
from function import *
class Log_inServer(FunctionServer):
    def __init__(self,mess,conn):
        super().__init__(mess,conn)
        self.user_id = mess["user_id"]
        self.user_password = mess["user_password"]
    def server_handle(self):
        dao = UserDao()
        user = dao.query_by_id(self.user_id)
        if not user:
            # 若无此用户
            resp = "用户不存在"
        else:
            # 验证密码
            if self.user_password == self.user_password:
                resp =  '登录成功'
            else:
                resp = "密码错误"
        self.conn.send(resp.encode())
        
class Log_inClient(FunctionClient):
    def __init__(self,clisocket,user):
        super().__init__(clisocket,user)

    def request(self):
        '''
        向服务器发送登录请求
        '''
        prepare_mess = {}
        prepare_mess['type'] = LOG_IN
        prepare_mess['user_id'] = self.user.user_id
        prepare_mess['user_password'] = self.user.user_password
        length = str(len(str(prepare_mess))).rjust(4,'0')
        mess = length+str(prepare_mess)
        self.clisocket.send(mess.encode())


    def response(self):
        resp = self.clisocket.recv(1024)
        return resp
