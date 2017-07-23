from selenium import webdriver
d = webdriver.Chrome()
d.get('http://www.wyl.cc/')
somethins = d.find_element_by_css_selector('.entry-title a').text
d.get('http://www.samwang.xyz/emlog/admin/')
d.find_element_by_id('user').send_keys('admin')
d.find_element_by_id('pw').send_keys('samwang0106.')
d.find_element_by_class_name('submit').click()
d.get('http://www.samwang.xyz/emlog/admin/twitter.php')
d.find_element_by_class_name('box').send_keys(somethins)
d.find_element_by_css_selector('.tbutton input').click()
d.quit()
