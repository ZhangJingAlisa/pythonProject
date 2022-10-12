from whereGoPO.base.base import Base
from time import sleep


class BookList(Base):
    def book_buy(self):
        return self.get_xpath('//*[@id="list_listInfo"]/ul[2]/li[1]/div/div[7]/a[1]')

    def book_list(self):
        self.book_buy().click()
        sleep(2)
