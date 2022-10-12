from datetime import date, datetime, timedelta
import xlrd


def input_date(n):
    # 根据传入的n,获取当前日期后几天的数据，timedelta表示偏移量
    return str(date.today() + timedelta(days=int(n)))


def read_excel(filename, index, isHead=False):
    xlsx = xlrd.open_workbook(filename)
    sheet = xlsx.sheet_by_index(index)

    data = []
    for i in range(sheet.nrows):
        if i == 0:
            if isHead:
                continue

        data.append(sheet.row_values(i))
    return data
