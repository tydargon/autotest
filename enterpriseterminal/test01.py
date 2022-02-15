# _*_ conding: UTF-8 _*_
import unittest
import HTMLTestRunner
import time

class UserTestCase(unittest.TestCase):

    def setUp(self):
        print("=====setup=======")
        self.name = "小D课堂"
        self.age = 29
        self.x = "xdclass"

    def tearDown(self):
        print("=====tearDown=======")
        self.assertTrue(self.x.upper(), "XDCLASS")


    def test_one(self):
        u"test_one方法"
        print("name:",self.name)
        self.assertEqual(self.name, "小D课堂", msg="名字不正确！！！")

    def test_two(self):
        print("=====is_upper=======")
        self.assertTrue(self.x.isupper(), msg="不是大写")

    def test_three(self):
        print("=====test_three=======")
        self.assertEqual(self.age, 29, msg="年龄一致！！！")

    def test_four(self):
        u"test_four方法说明"
        print("=====test_four=======")
        self.assertEqual(self.age, 29, msg="年龄一致！！！")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(UserTestCase("test_one"))
    suite.addTest(UserTestCase("test_four"))

    # runer = unittest.TextTestRunner(verbosity=2)
    # runer.run(suite)
    file_prefix = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    print(file_prefix)
    fp = open("./" + file_prefix + "_result.html", "wb")
    runer = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"小D课堂 测试报告", description=u"测试用例执行情况")
    runer.run(suite)
