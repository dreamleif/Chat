from db_helper import *
from table import *
from manage import *

# 数据库访问对象
class UserDao:
	    #构造函数
    def __init__(self):
        self.db_helper = DBHelper()  #创建DBHelper对象
        self.db_helper.open_conn()   #打开数据库连接

    #析构函数
    def __del__(self): 
        self.db_helper.close_conn()  #关闭数据库连接 

    #根据用户id号查询用户
    def query_by_id(self, user_id):         
        sql = "select * from user where user_id = '%s'" % user_id

        result = self.db_helper.do_query(sql)
        if not result:
            print("查询返回空对象")
            return None

        user_info = result[0]
        if not user_info:
            print("查询返回空对象")
            return None

        user_id = user_info[0]
        user_name = user_info[1]
        user_password = user_info[2]
        user_email = user_info[3]
        user_phone_number = user_info[4]
        return User(user_id, user_name, user_password,user_email,user_phone_number)

    def insert_user(self, user):  #插入对象
        sql = '''insert into user(user_id, user_name, password, e_mail,phone_number) \
                 values('%s','%s','%s','%s','%s')
        ''' % (user.user_id, user.user_name, user.user_password, user.user_email,user.user_phone_number)
        result = self.db_helper.do_update(sql)
        if not result:
            ret = "执行插入错误"
        else:
            ret = "执行结果，影响行数:%d" % result
        return ret
    
    # 修改用户信息
    def update_user(self, user):
        pass

    def query_all_user(self):
        print("do 1")

if __name__ == "__main__":
    db_helper = DBHelper()    #实例化数据访问对象
    db_helper.open_conn()   #打开数据库连接

    am = UserManage()  #实例化userManage对象

    # 根据订单编号查询
    user = am.query_by_id("lyf3351")
    print(user)

    # 插入
    new_user = User("lyf3351", "leif", "liyufei", "lyf3351@163.com","12332324444")
    am.insert_user(new_user)

    # 更新
    # new_user = user("201801010012", "C0012", 6, 666666.66)
    # am.update_user(new_user)

    # 查询全部
    # user_list = am.query_all_user()
    # for a in user_list:
    #     print(a)

    db_helper.close_conn()

