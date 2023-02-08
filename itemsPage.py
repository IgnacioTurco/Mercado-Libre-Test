import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class items:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.select_brand = (By.CSS_SELECTOR, '[aria-label="Ropa Deportiva"]')
        self.select_size = (By. CSS_SELECTOR, '[aria-label="S"]')
        self.total_results = (By. XPATH, '//*[@id="root-app"]/div/div[2]/aside/div[2]/span')
        self.prices = (By. CLASS_NAME, 'price-tag-fraction')
        self.titles = (By. XPATH, "//*[starts-with(@class,'ui-search-item__title')]")


    def click_brand(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_brand)).click()
    
    def click_size(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_size)).click()
    
    def total_numbers_results(self):
        text = self.driver.find_element(*self.total_results).text
        print(text)

    def assert_prices(self):
        array_price = []
        quantity = len(self.driver.find_elements(*self.prices))
        print(quantity)
        for i in range(quantity):
            array_price.append(self.driver.find_elements(*self.prices)[i].text)
        #price = [float(x) for x in array_price]
        final_array = sorted(array_price)
        print(final_array)
        
        tc = unittest.TestCase('__init__')
        tc.assertTrue (final_array[0] <= final_array[1] <= final_array[2] <= final_array[3] <= final_array[4])
        
    def order_titles(self):
        array_title = []
        number = len(self.driver.find_elements(*self.titles))
        print(number)
        for i in range(number):
            array_title.append(self.driver.find_elements(*self.titles)[i].text)
        array_title_ascend = sorted(array_title)
        for i in range(number):
            print(array_title_ascend[i])
