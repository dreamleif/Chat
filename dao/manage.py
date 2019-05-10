# manage.py
# 管理类
from table import *
from dao import *

class UserManage:
    def __init__(self):
        self.user_dao = UserDao()   #持有数据访问对象

    #根据订单号查询订单
    def query_by_id(self, user_id): 
        if not user_id:
            print("订单编号对象非法")
            return None
        if user_id == "":
            print("订单编号不能为空")
            return None
        return self.user_dao.query_by_id(user_id)

    # 查询所有订单
    def query_all_user(self):
        return self.user_dao.query_all_user()

    # 新增订单
    def insert_user(self, user): 
        if (not user.user_id) or user.user_id == "":
            print("用户id不能为空")
            return None

        return self.user_dao.insert_user(user)

    # 修改订单
    def update_user(self, user):
        if (not user.user_id) or user.user_id == "":
            print("订单编号不能为空")
            return

        if user.products_num < 1:
            print("商品数量非法")
            return

        if user.amt - 10.00 < 0.00001:  # 订单金额小于10元
            print("订单金额小于最低起购额度")
            return

        return self.user_dao.update_user(user)


