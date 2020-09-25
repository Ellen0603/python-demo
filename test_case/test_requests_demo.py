import allure
import requests




def test_demo():
    r = requests.get("https://www.baidu.com/")
    print(r.text)

def test_demo_1():
    r = requests.request("GET","https://www.baidu.com/")
    print(r.text)

def test_demo_2():
    demo = requests.session()
    s = demo.request(method="GET",url="https://www.baidu.com/")
    print(s.text)

def test_demo_3():
    params = {"accountName":"acbd066"}
    r = requests.request("GET","http://qa.yansl.com:8084/acc/getAccInfo",params = params)
    print(r.text)


def test_demo_4():
    r = requests.request("GET","http://qa.yansl.com:8084/acc/getAllAccs/{}/{}".format(1,3))
    print(r.text)

def test_demo_5(pub_data):
    headers = {"token":pub_data["token"]}
    params = {"phone":"13621452658"}
    r = requests.request("GET","http://qa.yansl.com:8084/cst/getCustomer",params = params,headers = headers)
    print(r.json())

@allure.feature("产品模块")
@allure.story("下载库存信息")
@allure.title("demo_6")
def test_demo_6(pub_data):
    with allure.step("prepare requests data"):pass
    params = {"pridCode":"2653142"}
    headers = {"token":pub_data["token"]}
    with allure.step("send requests"):pass
    r = requests.request("GET","http://qa.yansl.com:8084/product/downProdRepertory",params = params,headers = headers)
    with allure.step("attachment"):
        allure.attach("requests headers","info",allure.attachment_type.TEXT)
    with open("a.xls","wb") as f:
        f.write(r.content)


@allure.feature("用户模块")
@allure.story("用户登录")
@allure.title("demo_7")
def test_demo_7():
    with allure.step("request data"):pass
    data = {"pwd": "123qvba",
  "userName": "acbd066"}
    with allure.step("send request"):pass
    r = requests.request("POST","http://qa.yansl.com:8084/login",json = data)
    print(r.text)


@allure.feature("用户模块")
@allure.story("用户冻结")
@allure.title("demo_8")
def test_demo_8(pub_data):
    data = {"userName":"acbd066"}
    headers = {"token":pub_data["token"]}
    r = requests.request("POST","http://qa.yansl.com:8084/user/lock",data = data,headers = headers)
    print(r.text)

@allure.feature("用户模块")
@allure.story("用户解冻")
@allure.title("demo_9")
def test_demo_9(pub_data):
    data = {"userName": "acbd066"}
    headers = {"token": pub_data["token"]}
    r = requests.request("POST", "http://qa.yansl.com:8084/user/unLock", data=data, headers=headers)
    print(r.text)



@allure.feature("产品模块")
@allure.story("盘点库存")
@allure.title("demo_10")
def test_demo_10(pub_data):
    files = {"file":open("a.xls","rb")}
    headers = {"token":pub_data["token"]}
    r = requests.request("POST", "http://qa.yansl.com:8084/product/uploaProdRepertory", files=files, headers=headers)
    print(r.text)
    print("url:",r.request.url)





























