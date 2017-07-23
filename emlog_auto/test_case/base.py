from selenium import webdriver
import unittest,sys
base_url = 'http://192.168.2.229/blog/'



def by_css(d,ele):
    return d.find_element_by_css_selector(ele)
def by_name(d,ele):
    return d.find_element_by_name(ele)
def by_text(d,ele):
    return d.find_element_by_partial_link_text(ele)
def by_xpath(d,ele):
    return d.find_element_by_xpath(ele)
def save_img(d,files):
    return d.get_screenshot_as_file(files)
def by_class(d,ele):
    return d.find_element_by_class_name(ele)


class brunit(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.filename= ''

    def tearDown(self):
        #self.filename = "../case_img/"+str(sys._getframe().f_code.co_name)+".jpg"
        save_img(d=self.dr,files=self.filename)
        self.dr.quit()
