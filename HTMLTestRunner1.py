import unittest
import time
import requests
from unittest import mock
import HTMLTestRunner
from base.demo import RunMain
class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()
    def test_01(self):
        url = 'http://op.juhe.cn/shanghai/police?key=eec88d051b6fcf5c5373f870a7b21ab9'
        data = {'key': 'ec88d051b6fcf5c5373f870a7b21ab9'}
        res = self.run.run_main(url,'GET',data)
        self.assertEqual(res['error_code'],10001,"测试失败")
        print("这是第一个测试")
    def test_02(self):

        url = 'http://op.juhe.cn/shanghai/police?key=eec88d051b6fcf5c5373f870a7b21ab9'
        data = {'key': 'ec88d051b6fcf5c5373f870a7b21ab9'}
        res = self.run.run_main(url,'POST',data)
        self.assertEqual(res['error_code'], 10001,"测试失败")
        print('这是第二个测试方法')

if __name__ == '__main__':
    now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    fp = open('./reports/htmlreport.html','wb')
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='welcome to this web')
    runner.run(suite,rerun=0,save_last_run=False)
    fp.close()
