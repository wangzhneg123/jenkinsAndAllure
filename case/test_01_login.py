# coding : utf-8
import requests
import pytest
from common.config import *
from common.Util_readFile import readFile_excelContent

def getvalue():
    return readFile_excelContent("value.xlsx", "Sheet1")


class Test_login():
    def top(self,name,pwd):
        headers = {
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/x-www-form-urlencoded;charset = UTF-8"

        }
        bodys = {
            "username": name,
            "password": pwd
        }
        data = requests.post(url=login_url_downstage, data=bodys, headers=headers)
        return data.json()

    def test_yes(self):
       """
       正确的用户名  和正确的密码
       """
       json = self.top("wang123456","wang123456")
       assert json["code"] == 1
       assert json["url"] == "/projects/admin.php/index/index.html"

    @pytest.mark.parametrize(("name","pwd","msg1"),getvalue())
    def test_no(self,name,pwd,msg1):
        """
        错误的用户名 或者错误的密码
        :param name: 用户名
        :param pwd:  密码
        :param msg:  断言信息
        """
        json = self.top(name, pwd)
        assert json["msg"] ==msg1




