import pytest
@pytest.fixture(scope="class") # 作用域
def aa():
    print("fixture函数被运行了")
    return 11

@pytest.fixture() # 作用域
def bb():
    print("fixture函数被运行了")
    return 11

@pytest.mark.usefixtures("aa","bb")
class Test111():
    def test_aa(self):
        print(111)
    def test_bb(self):
        print(111)