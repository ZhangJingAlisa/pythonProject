from whereGo.where_book import book_ticket
from whereGo.base_function import read_excel
import pytest

data = read_excel('../whereGoPO/data/whereGO.xlsx', 0, True)

@pytest.mark.parametrize(['start', 'end', 'n', 'name', 'idCard'], data)
def test_book_ticket(start, end, n, name, idCard):
    book_ticket(start, end, n, name, idCard)


if __name__ == '__main__':
    pytest.main(['-s', 'test_where.py'])
