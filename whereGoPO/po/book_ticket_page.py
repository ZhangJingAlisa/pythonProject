from whereGoPO.base.base import Base
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


class BookTicket(Base):
    def book_start(self):
        return self.get_name('fromStation')

    def book_end(self):
        return self.get_name('toStation')

    def book_date(self, date):
        self.get_name('date').send_keys(Keys.CONTROL, 'a')  # 全选日期
        self.get_name('date').send_keys(Keys.BACK_SPACE)  # 回退，即删除之前的日期数据
        self.get_name('date').send_keys(date)

    def book_btn(self):
        return self.get_name('stsSearch')

    def action_even(self):
        action = ActionChains(self.driver)  # 实例化鼠标事件
        # 下面代码模拟选择了一个数据后将鼠标移出去后点击一下
        action.move_by_offset(0, 0)
        action.click()
        action.perform()

    def book_ticket(self, start, end, date):
        # 输入正确的出发站和到达站、日期等数据
        # self.book_start().clear()  # 清除内容
        self.book_start().send_keys(start)
        self.action_even()

        # self.book_end.clear()  # 清除内容
        self.book_end().send_keys(end)
        self.action_even()

        # 输入日期数据
        self.book_date(date)
        self.action_even()

        # 点击预定
        self.book_btn().click()
        sleep(2)
