import sys
sys.path.append("..")
from base import *
from time import sleep
from selenium.webdriver.support.ui import Select
role_select_ele = '#role'
username_ele = '#login'
password_ele = "#password"
confirm_pwd_ele = '#password2'
news_ischeck_ele = 'ischeck'
add_user = "button"
user_url = 'admin/user.php'
row_select = ['writer','admin']
news_select = ['n','y']


# def add_user(d,usr='admin',psd,pows,news=news_select[1]):
#     Select(by_css(role_select_ele)).select_by_value(pows)
#     by_css(d,username_ele).send_keys(usr)
#     by_css(d,password_ele).send_keys(psd)
#     by_css(d,confirm_pwd_ele).send_keys(psd)
#     by_css(d,add_user).click()
#     if pows==row_select[0]:
#         Select(by_css(news_ischeck_ele)).select_by_value(news)


def select_admin(d):
    Select(by_css(d,role_select_ele)).select_by_value('admin')

def select_writer(d,auth=news_select[0]):
    Select(by_css(d,role_select_ele)).select_by_value(row_select[0])
    Select(by_name(d,news_ischeck_ele)).select_by_value(auth)

def add_user(d,usr='admin',psd='123456',psd2='123456'):
    by_css(d,username_ele).send_keys(usr)
    sleep(1)
    by_css(d,password_ele).send_keys(psd)
    sleep(1)
    by_css(d,confirm_pwd_ele).send_keys(psd2)
    sleep(3)
    by_class(d,add_user).click()
    sleep(3)
