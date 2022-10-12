from whereGo.base_function import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


def book_ticket(start, end, n, name, idCard):
    driver = get_driver()
    open_url('https://train.qunar.com/')
    sleep(2)
    action = ActionChains(driver)  # 实例化鼠标事件

    # 输入正确的出发站和到达站、日期等数据
    get_name('fromStation').clear()  # 清除内容
    get_name('fromStation').send_keys(start)
    # 下面代码模拟选择了一个数据后将鼠标移出去后点击一下
    action.move_by_offset(0, 0)
    action.click()
    action.perform()

    get_name('toStation').clear()  # 清除内容
    get_name('toStation').send_keys(end)
    # 下面代码模拟选择了一个数据后将鼠标移出去后点击一下
    action.move_by_offset(0, 0)
    action.click()
    action.perform()

    # 输入日期数据
    get_name('date').send_keys(Keys.CONTROL, 'a')  # 全选日期
    get_name('date').send_keys(Keys.BACK_SPACE)  # 回退，即删除之前的日期数据
    get_name('date').send_keys(input_date(n))
    # 下面代码模拟选择了一个数据后将鼠标移出去后点击一下
    action.move_by_offset(0, 0)
    action.click()
    action.perform()

    # 点击预定
    get_name('stsSearch').click()

    sleep(2)
    # 点击购买
    get_xpath('//*[@id="list_listInfo"]/ul[2]/li[1]/div/div[7]/a[1]').click()

    sleep(2)
    # 添加身份证信息
    get_name('pName_0').send_keys(name)
    get_name('pCertNo_0').send_keys(idCard)

    sleep(2)
    # close()
