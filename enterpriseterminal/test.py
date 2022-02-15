from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = "https://ralph.test.zyde.vip/static/login/login.html"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
print(driver.title)

sleep(3)
#登录操作，输入用户名
# driver.find_element_by_name('username').clear()
driver.find_element(By.NAME, "username").send_keys("1995yh13311796165")
#输入密码
# driver.find_element_by_name('password').clear()
driver.find_element(By.NAME,'password').send_keys('123456')
try:
#点击登录操作

    driver.find_element(By.XPATH,'//*[@id="form"]/div[2]/button').click()
except:
    driver.get_screenshot_as_file('./error_png.png')

#判断登录是否成功
user_info_ele = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/section/header/div/div[3]/span[3]/span')
print("=======测试结果=======\n",user_info_ele.text)

sleep(2)
#定位任务管理菜单元素
# driver.find_element_by_xpath('//*[@id="root"]/div/div/section/section/aside/div/ul/li[3]/a').click()
# ActionChains(driver).move_to_element(menu_ele).perform()
