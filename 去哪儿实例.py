from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import date, datetime, timedelta


def input_date(n):
    # 根据传入的n,获取当前日期后几天的数据，timedelta表示偏移量
    return str(date.today() + timedelta(days=int(n)))


driver = webdriver.Chrome()

driver.get("https://train.qunar.com/")
driver.maximize_window()  # 窗口最大化
action = ActionChains(driver)  # 实例化鼠标事件

# 输入正确的出发站和到达站、日期等数据
driver.find_element('name', 'fromStation').send_keys('北京')
# 下面代码模拟选择了一个数据后将鼠标移出去后点击一下
action.move_by_offset(0, 0)
action.click()
action.perform()

driver.find_element('name', 'toStation').send_keys('上海')
# 下面代码模拟选择了一个数据后将鼠标移出去后点击一下
action.move_by_offset(0, 0)
action.click()
action.perform()

# 输入日期数据
driver.find_element('name', 'date').send_keys(Keys.CONTROL, 'a')  # 全选日期
driver.find_element('name', 'date').send_keys(Keys.BACK_SPACE)  # 回退，即删除之前的日期数据
driver.find_element('name', 'date').send_keys(input_date(4))
# 下面代码模拟选择了一个数据后将鼠标移出去后点击一下
action.move_by_offset(0, 0)
action.click()
action.perform()

# 点击预定
driver.find_element('name', 'stsSearch').click()

sleep(2)
# 点击购买
driver.find_element(By.XPATH, '//*[@id="list_listInfo"]/ul[2]/li[1]/div/div[7]/a[1]').click()

sleep(2)
# 添加身份证信息
driver.find_element('name', 'pName_0').send_keys('张三')
driver.find_element('name', 'pCertNo_0').send_keys('531255199807253662')

sleep(3)

driver.quit()
