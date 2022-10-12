from selenium.webdriver.common.by import By


class Base():
    def __init__(self, driver):
        self.driver = driver

    def get_name(self, element):
        return self.driver.find_element('name', element)

    def get_xpath(self, element):
        return self.driver.find_element(By.XPATH, element)