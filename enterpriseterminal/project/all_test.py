import unittest
import time
import login
import HTMLTestRunner

#创建测试集合
def create_suite():
    print("测试开始")
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(login.LoginTestCase))
    return suite

if __name__ == '__main__':
    suite = create_suite()

    #文件名中加了当前时间，为了每次生成不同的测试报告
    file_prefix = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())

    #创建测试报告，此时这个文件还是空文件 wb 以二进制格式打开一个文件，只用于写入，如果文件存在则覆盖，不存在创建
    fp = open("Report/" + file_prefix + "_result.html", "wb")

    #stream 定义一个测试报告写入的文件，title 就是标题，description就是描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"企业端  测试报告", description="企业端进件支付流程测试")
    runner.run(suite)
    fp.close()