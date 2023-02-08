import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from indexPage import index
from itemsPage import items
import time

class Test(unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument('start-maximized')
        option.add_argument('--headless')
        self.driver = webdriver.Chrome('Chromedriver.exe', options=option)
        self.driver.get('https://www.mercadolibre.com.ar/')
        self.driver.implicitly_wait(5)
        self.index = index(self.driver)
        self.items = items(self.driver)

    def test_search_item(self):
        self.index.delete_cookie()
        #time.sleep(3)
        self.index.search_item('remera')
        #time.sleep(3)
        self.items.click_brand()
        time.sleep(5)
        self.items.click_size()
        time.sleep(3)
        self.items.total_numbers_results()
        time.sleep(3)
        self.items.assert_prices()
        time.sleep(3)
        self.items.order_titles()
        time.sleep(3)


def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()