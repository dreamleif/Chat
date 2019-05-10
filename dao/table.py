'''
聊天室V1.0
数据访问对象
'''
class User:
    def __init__(self,user_id,user_name,user_password,user_email,user_phone_number):
        """
        用户对象
        user_id:用户id
        user_name:用户昵称
        passward:用户密码
        e_mail:用户邮箱
        position:用户当前位置
        """
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_email = user_email
        self.user_phone_number = user_phone_number
    
    def __str__(self):  
        return "id:%s,name:%s"%(self.user_id,self.user_name)
    def __rep__(self):
        return self.__str__()


class Room:
    def __init__(self,room_id,room_theme,room_info,room_group,messages):
        """
        聊天室对象
        room_id:聊天室id
        room_info:聊天室信息
        room_theme:聊天室主题
        room_group:聊天室成员
        messages :当前聊天室聊天记录
        """
        self.room_id = room_id
        self.room_info = room_info
        self.room_theme = room_theme
        self.room_group = room_group
        self.messages = messages
class Message:
    def __init__(self,):
        """
        聊天记录对象
        self.user:用户对象 
        self.message:聊天信息str
        self.time:时间
        """
        self.user = user
        self.message = message
        self.time = time
