from config import *
import sys
sys.path.append("./dao")
from table import *
from dao import *
from function import *
class RegisterServer(FunctionServer):
    def __init__(self,mess,conn):
        super().__init__(mess,conn)
        self.user = User(mess["user_id"],mess["user_name"],mess["user_password"],mess["user_email"],mess["user_phone_number"])
    
    def server_handle(self):
        dao = UserDao()
        resp = dao.insert_user(self.user)
        self.conn.send(resp.encode())
        
class RegisterClient(FunctionClient):
    def __init__(self,user,clisocket):
        super().__init__(user,clisocket)
    
    def request(self):
        prepare_mess = {}
        prepare_mess['type'] = REGISTER
        prepare_mess['user_name'] = self.user.user_name
        prepare_mess['user_id'] = self.user.user_id
        prepare_mess['user_password'] = self.user.user_password
        prepare_mess['user_email'] = self.user.user_email
        prepare_mess['user_phone_number'] = self.user.user_phone_number
        length = str(len(str(prepare_mess))).rjust(4,'0')
        mess = length+str(prepare_mess)
        self.clisocket.send(mess.encode())

    def response(self):
        resp = self.clisocket.recv(1024)
        return resp
        
