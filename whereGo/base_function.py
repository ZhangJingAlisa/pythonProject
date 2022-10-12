from datetime import date, datetime, timedelta
from selenium import webdriver
import xlrd
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def input_date(n):
    # 根据传入的n,获取当前日期后几天的数据，timedelta表示偏移量
    return str(date.today() + timedelta(days=int(n)))


def get_driver():
    return driver


def open_url(url):
    driver.get(url)
    driver.maximize_window()  # 窗口最大化


def get_name(element):
    return driver.find_element('name', element)


def get_xpath(element):
    return driver.find_element(By.XPATH, element)


def close():
    driver.close()


def read_excel(filename, index, isHead = False):
    xlsx = xlrd.open_workbook(filename)
    sheet = xlsx.sheet_by_index(index)

    data = []
    for i in range(sheet.nrows):
        if i == 0:
            if isHead:
                continue

        data.append(sheet.row_values(i))
    return data


if __name__ == '__main__':
    print(read_excel('../whereGoPO/data/whereGO.xlsx', 0, True))
