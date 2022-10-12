from selenium import webdriver
from selenium.webdriver.common.by import By

# 将全部的方法打包
def get_element(driver, *loc):
    e = driver.find_element(*loc)
    return e

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")

    # get_element(driver, By.ID, "kw").send_keys("selenium")
    # get_element(driver, By.ID, "su").click()

    loc = (By.ID, "kw")
    loc2 = (By.ID, "su")
    get_element(driver, *loc).send_keys("selenium")
    get_element(driver, *loc2).click()