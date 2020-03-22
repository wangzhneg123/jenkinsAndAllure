import  allure

class Test01():

    @allure.issue("http://123.57.223.10:8088/zentao/bug-view-1.html")
    def test01(self):
        """
        这是一个bug 在禅道中的路径
        :return:
        """
        pass
    @allure.testcase("http://123.57.223.10:8088/zentao/testcase-view-4-1.html")
    def test02(self):
        """
        这是一个用例 禅道中的
        :return:
        """
        pass