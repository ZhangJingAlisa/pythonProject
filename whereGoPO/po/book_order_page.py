from whereGoPO.base.base import Base
from time import sleep


class BookOrder(Base):
    def book_order_name(self):
        return self.get_name('pName_0')

    def book_order_idCard(self):
        return self.get_name('pCertNo_0')

    def book_order(self, name, idCard):
        self.book_order_name().send_keys(name)
        self.book_order_idCard().send_keys(idCard)
        sleep(2)
