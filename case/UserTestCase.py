import unittestfrom util.RequestUtil import RequestUtilhost = 'https://api.xdclass.net'class UserTestCase(unittest.TestCase):    def testLogin(self):        """        登录操作用例        """        request = RequestUtil()        url = host + '/pub/api/v1/web/web_login'        data = {'phone':'13311796165', 'pwd':'Tyl628919'}        headers = {'Content-Type': 'application/x-www-form-urlencoded'}        result = request.request(url, 'post', param=data, headers=headers)        self.assertEqual(result['code'], 0, '业务状态码不正常')        self.assertTrue(len(result['data']) > 0, '分类列表为空')        # print(result)        name = result['data']['name']        # print(name)        if name == '龙':            print('验证通过，登录名称为：{0}'.format(name))if __name__ == '__main__':    unittest.main(verbosity=2)