class Register(Function):
    def __init__(self,user):
        self.user = user
    
    def server_handle(self):
        user_ip = self.user.user_ip
        user_name = self.user.user_name
        user_password = self.user.user_password
        user_phone_number = self.user.user_phone_number
        user_email = self.user.user_email

    
