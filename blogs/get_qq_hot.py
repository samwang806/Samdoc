from selenium import webdriver
import time
from time import *
from selenium.webdriver.support.ui import Select

class QQDailyHot():
    def __init__(self):#在每个用力执行前执行
        self.dr = webdriver.Chrome()
        self.title,self.content = self.get_title_and_content()

    def get_daily_hot_url(self):
        return self.by_css('#todaytop a').get_attribute('href')

    def get_title_and_content(self):
        self.dr.get('http://www.qq.com')
        url = self.get_daily_hot_url()
        self.dr.get(url)
        title = self.by_id('sharetitle').text
        content = self.by_id('articleContent').get_attribute('innerHTML')
        return (title,content)

    def by_id(self, the_id):
        return self.dr.find_element_by_id(the_id)

    def by_css(self, css):
        return self.dr.find_element_by_css_selector(css)

    def by_name(self, name):
        return self.dr.find_element_by_name(name)

    def by_class(self,name):
        return self.dr.find_element_by_class_name(name)

    def by_xpath(self,the_xpath):
        return self.dr.find_element_by_xpath(the_xpath)


    def login_as_admin(self):
        self.by_id('user').send_keys('admin')
        self.by_id('pw').send_keys('samwang0106.')
        self.by_class('submit').click()

    def login(self,username,password):
        self.by_id('user_login').send_keys(username)
        self.by_id('user_pass').send_keys(password)
        self.by_class('wp-submit').click()


    def set_content(self,text):
        text = text.strip()
        # text.replace('\\n','')
        # sleep(1)
        # print(text)
        # $('#list').html(`
        # <ul>
        #   <li>first</li>
        #   <li>second</li>
        # </ul>
        # `.trim());
        #js = 'document.getElementById("content_ifr").contentWindow.document.body.innerHTML = \'%s\''%(text)
        js = 'document.querySelector(".ke-edit-iframe").contentWindow.document.body.innerHTML =`%s`'%(text)
        #print(js)
        sleep(1)
        #print(js)
        self.dr.execute_script(js)


    def create_post_from_qq(self):
        self.dr.get('http://www.samwang.xyz/emlog/admin/')
        self.login_as_admin()
        self.dr.get('http://www.samwang.xyz/emlog/admin/write_log.php')
        self.by_id('title').send_keys(self.title)
        sleep(3)
        self.set_content(self.content)
        # self.by_css('span[data-name="source"] span').click()
        sleep(3)
        Select(self.by_id("sort")).select_by_value("1")
        sleep(1)
        # contents = self.content.strip()
        # print(contents)
        #self.dr.refresh()

        #ifs = self.by_class('ke-edit-iframe')
        #self.dr.switch_to.frame(ifs)
        #self.by_class('ke-content').send_keys(self.content)
        # sleep(3)
        # self.by_class('ke-edit-textarea').send_keys(contents)
        #self.set_content(self.content)
        # sleep(3)
        self.by_css('#post_button > input:nth-child(3)').click()
        sleep(3)


    def quit(self):
        self.dr.quit()


if __name__ == '__main__':
    daily_hot = QQDailyHot()
    daily_hot.create_post_from_qq()
    daily_hot.quit()
