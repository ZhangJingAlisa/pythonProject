# 导入driver
from selenium import webdriver
# 导入睡眠时间
from time import sleep

# 获取谷歌浏览器
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
sleep(3)
# 获取输入框的ID，并输入指定的内容
driver.find_element_by_id("kw").send_keys("selenium")
sleep(3)
# 获取按钮的ID，并点击按钮
driver.find_element_by_id("su").click()
sleep(3)

# 退出浏览器驱动
driver.quit()

# 将上面的方法进行封装
class testCode(object):
    def __int__(self):
        self.driver = webdriver.Chrome()

    def test(self):
        self.driver.get("http://www.baidu.com")
        sleep(3)
        # 获取输入框的ID，并输入指定的内容
        self.driver.find_element_by_id("kw").send_keys("selenium")
        sleep(3)
        # 获取按钮的ID，并点击按钮
        self.driver.find_element_by_id("su").click()
        sleep(3)

if __name__ == '__main__':
    # test
    case = testCode()
    case.test()