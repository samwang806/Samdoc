from selenium import webdriver
import unittest,sys
from page_ele import login_page
from base import *

class login_test(brunit):
    def open_url(self):
        self.url = base_url+login_page.login_url
        self.dr.get(self.url)

    def test_login_success(self):
        self.open_url()
        login_page.login_action(d=self.dr)
        self.assertIn('admin',by_css(self.dr,login_page.login_success_ele).text)
        self.filename = "./case_img/"+str(sys._getframe().f_code.co_name)+".jpg"

    def test_login_user_error(self):
        self.open_url()
        login_page.login_action(d=self.dr,usr='admssadm')
        self.assertIn('用户名错误',by_css(self.dr,login_page.login_error_ele).text)
        self.filename = "./case_img/"+str(sys._getframe().f_code.co_name)+".jpg"

    def test_login_pwd_error(self):
        self.open_url()
        login_page.login_action(d=self.dr,psd='asd')
        self.assertIn('密码错误',by_css(self.dr,login_page.login_error_ele).text)
        self.filename = "./case_img/"+str(sys._getframe().f_code.co_name)+".jpg"

    def test_back_index(self):
        self.open_url()
        by_text(d=self.dr,ele='返回首页')
        self.assertIn(self.url,self.dr.current_url)
        self.filename = "./case_img/"+str(sys._getframe().f_code.co_name)+".jpg"

if __name__ == '__main__':
    unittest.main()
