from selenium import webdriver
import unittest,sys
from page_ele import login_page,user_page
from base import *
from time import sleep


class add_user_test(brunit):
    def open_url(self):
        self.url = base_url+login_page.login_url
        self.dr.get(self.url)

    def login_success(self):
        self.open_url()
        login_page.login_action(d=self.dr)

    def setUp(self):
        self.dr = webdriver.Chrome()
        self.login_success()
        self.dr.get(base_url+user_page.user_url)
        self.filename= ''
        by_text(self.dr,'添加用户').click()

    def test_add_admin_user(self):
        #user_page.select_writer(d=self.dr)
        user_page.select_admin(d=self.dr)
        sleep(1)
        user_page.add_user(d=self.dr,usr='auto_add2')
        sleep(1)
        self.filename = "./case_img/"+str(sys._getframe().f_code.co_name)+".jpg"

if __name__ == '__main__':
    unittest.main()
