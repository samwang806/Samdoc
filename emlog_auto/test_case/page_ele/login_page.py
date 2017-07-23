import sys
sys.path.append("..")
from base import *

login_user_ele = '#user'
login_psd_ele = '#pw'
login_button = '.submit'
login_back_index_ele = '.back'
login_success_ele = '.msg2 a'
login_error_ele = '.login-error'
login_url = 'admin/'


def login_action(d,usr='admin',psd='admin1'):
    by_css(d,login_user_ele).send_keys(usr)
    by_css(d,login_psd_ele).send_keys(psd)
    by_css(d,login_button).click()
