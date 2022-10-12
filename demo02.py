from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class TestCode(object):
    def __int__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        # 实现窗口最大化
        self.driver.maximize_window()
        sleep(1)

    def test_id(self):
        # find_element_by_id：返回的值是唯一的
        self.driver.find_element_by_id("kw").send_keys("selenium")
        # <class 'selenium.webdriver.remote.webelement.WebElement'>

        self.driver.find_element_by_id("su").click()
        sleep(3)
        self.driver.quit()

    def test_name(self):
        # find_element_by_name：可能返回多个元素，返回第一个
        # self.driver.find_elements_by_name()：返回一个集合

        self.driver.find_element_by_name("wd").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        sleep(3)
        self.driver.quit()

    def test_linkText(self):
        self.test_id()
        self.driver.find_element_by_link_text("百度首页").click()
        sleep(3)

    def test_partial_link_text(self):
        self.test_id()
        self.driver.find_element_by_partial_link_text("百度首页").click()
        sleep(3)

    def test_xpath(self):
        self.driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        sleep(3)

    def test_tag(self):
        # 返回多个，如果需要返回一个，则直接用数组即可
        self.driver.find_element_by_tag_name('input')[0]
        print(input)

    def test_css_selector(self):
        self.driver.find_element_by_css_selector("#kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        sleep(3)

    def test_className(self):
        self.driver.find_element_by_class_name("s_ipt").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        sleep(3)

    def test_all(self):
        self.driver.find_element(By.id,value="kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        sleep(3)

if __name__ == '__main__':
    case = TestCode()
    # case.test_id()
    # case.test_name()
    # case.test_linkText()
    # case.test_partial_link_text()
    # case.test_xpath()
    # case.test_tag()
    # case.test_css_selector()
    # case.test_className()
    case.test_all()