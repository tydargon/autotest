from selenium.webdriver.common.by import Byfrom po.pages.base_page import BasePageclass LoginPage(BasePage):    URL = 'https://accounts.douban.com/passport/login'    USERNAME = (By.ID, 'username')    PASSWORD = (By.ID, 'password')    PASSlOGIN = (By.CLASS_NAME, 'account-tab-account on')    def __init__(self, driver):        super().__init__(driver = driver, url = self.URL)    def login(self):        self.open()        #*代表一个的list        self.find_element(*self.PASSlOGIN).click()        self.send_keys(webElement = self.find_element(*self.USERNAME), keys = '13311796165')        self.send_keys(webElement = self.find_element(*self.PASSWORD), keys = 'Tyl628919')