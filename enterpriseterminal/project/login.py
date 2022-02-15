import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        print("测试开始")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.base_url = "https://ralph.test.zyde.vip/static/login/login.html"
        self.driver.get(self.base_url)

    def tearDown(self):
        print("单个测试用例结束")
        self.driver.quit()

    def test_login(self):
        u"登录单个测试用例"
        driver = self.driver
        # 登录操作，输入用户名
        driver.find_element(By.NAME, 'username').clear()
        driver.find_element(By.NAME, "username").send_keys("1995yh13311796165")
        # 输入密码
        driver.find_element(By.NAME, 'password').clear()
        driver.find_element(By.NAME, 'password').send_keys('123456')

        sleep(2)
        try:
            # 点击登录操作
            driver.find_element(By.XPATH, '//*[@id="form"]/div[2]/button').click()
        except:
            driver.get_screenshot_as_file('./error_png.png')

        sleep(2)
        # 判断登录是否成功
        user_info_ele = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/section/header/div/div[3]/span[3]/span')
        print("=======测试结果=======")
        print(user_info_ele.text)
        user_info_ele = user_info_ele.text
        self.assertEqual(user_info_ele, u"1995yh13311796165", msg="登录失败！")

if __name__ == "__main__":
    unittest.main()