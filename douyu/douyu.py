from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.douyu.com/directory/all")
driver.maximize_window()

while True:
    sleep(2)
    # 设置页面滚动到的位置，尽量设置超过电脑屏幕的大小，这样会滚到最底下
    js_str = "window.scrollTo(0, 10000)"
    # 执行js代码
    driver.execute_script(js_str)

    sleep(2)

    # 获取整个页面的每一个项
    lis = driver.find_elements(By.CLASS_NAME, "layout-Cover-item")
    # 打印获取的条数
    print(len(lis))

    # 遍历获取的每一个项，将里面的内容打印出来
    for li in lis:
        info = {}
        info["title"] = li.find_element(By.CLASS_NAME, "DyListCover-intro").text
        info["username"] = li.find_element(By.CLASS_NAME, "DyListCover-userName").text
        info["hot"] = li.find_element(By.CLASS_NAME, "DyListCover-hot").text
        info["type0"] = li.find_element(By.CLASS_NAME, "DyListCover-zone").text

        print(info)

    # 获取下一页
    next_page = driver.find_element(By.XPATH, '//*[@id="listAll"]/section[2]/div[2]/div/ul/li[9]')
    # 如果下一页可以点击，则进行点击，否则退出循环
    if next_page.is_enabled():
        next_page.click()
    else:
        break
sleep(5)
driver.quit()
