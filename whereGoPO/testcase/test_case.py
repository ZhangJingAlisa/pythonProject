from whereGoPO.common.function import read_excel, input_date
from selenium import webdriver
from whereGoPO.po.book_ticket_page import BookTicket
from whereGoPO.po.book_list_page import BookList
from whereGoPO.po.book_order_page import BookOrder
import pytest

data = read_excel('../data/whereGO.xlsx', 0, True)


class TestCase():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://train.qunar.com/')
        self.driver.maximize_window()  # 窗口最大化

    @pytest.mark.parametrize(['start', 'end', 'n', 'name', 'idCard'], data)
    def test_book(self, start, end, n, name, idCard):
        book_ticket1 = BookTicket(self.driver)
        book_list1 = BookList(self.driver)
        book_order1 = BookOrder(self.driver)

        book_ticket1.book_ticket(start, end, input_date(n))
        book_list1.book_list()
        book_order1.book_order(name, idCard)

    def teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main()
