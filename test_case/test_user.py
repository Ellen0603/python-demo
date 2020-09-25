import random

from tools.api import request_tool

'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''




def test_signup(pub_data):
    pub_data["username"] = "自动生成 字符串 1,5 数字 acbd"
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户注册'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/signup"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "注册成功"  # 预期结果
    json_data='''{
  "phone": "自动生成 手机号",
  "pwd": "123qvba",
  "rePwd": "123qvba",
  "userName": "${username}"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)



def test_login(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "登录成功"  # 预期结果
    json_data='''{"pwd": "123qvba", "userName": "${username}"}'''

    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"token": "$['data']['token']"}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(json_path=json_path,method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)
#
#

# def test_charge(pub_data,db):
#     res = db.select_execute("SELECT account_name FROM `t_cst_account` WHERE STATUS=0 AND account_name IS NOT NULL;")
#     pub_data["account_name"] = random.choice(res)[0]
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '用户登录'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/acc/charge"  # 接口地址
#     headers = {}
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     json_data='''{
#   "accountName": "${account_name}",
#   "changeMoney": 0
# }'''
#
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)


def test_changepwd(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '修改密码'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/user/changepwd"  # 接口地址
    headers = {"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = "修改成功1"  # 预期结果
    json_data='''{
  "newPwd": "123qvqd",
  "oldPwd": "123qvba",
  "reNewPwd": "123qvqd",
  "userName": "${username}"
}'''


    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_relogin(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '登录验证'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "登录成功"  # 预期结果
    json_data='''{"pwd": "123qvqd", "userName": "${username}"}'''

    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"token": "$['data']['token']"}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(json_path=json_path,method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)
#































