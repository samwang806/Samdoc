from selenium import webdriver
import time
from time import *
from selenium.webdriver.support.ui import Select


dr = webdriver.Chrome()
dr.maximize_window()
dr.implicitly_wait(30)
dr.get('https://mp.weixin.qq.com/mp/homepage?__biz=MzI5ODU1MzkwMA==&hid=2&sn=2244b86ace89bcd5c48a4b910462bf64#wechat_redirect')
sleep(4)
url_ele = dr.find_elements_by_css_selector('.js_post')
sleep(1)
url_list = []
for i in url_ele:
    url_list.append(i.get_attribute('href'))
    sleep(1)
print(url_list)
dr.get('http://www.samwang.xyz/emlog/admin/')
dr.find_element_by_id('user').send_keys('admin')
dr.find_element_by_id('pw').send_keys('samwang0106.')
dr.find_element_by_class_name('submit').click()
sleep(2)

for x in url_list:
    dr.get(x)
    sleep(2)
    titles = dr.find_element_by_id('activity-name').text
    text = dr.find_element_by_id('js_content').get_attribute('innerHTML')
    text = text.strip()
    dr.get('http://www.samwang.xyz/emlog/admin/write_log.php')
    sleep(3)
    dr.find_element_by_id('title').send_keys(titles)
    sleep(3)
    js = 'document.querySelector(".ke-edit-iframe").contentWindow.document.body.innerHTML =`%s`'%(text)
    sleep(1)
    dr.execute_script(js)
    sleep(3)
    Select(dr.find_element_by_id("sort")).select_by_value("8")
    sleep(1)
    dr.find_element_by_css_selector('#post_button > input:nth-child(3)').click()
    sleep(3)
dr.quit()
