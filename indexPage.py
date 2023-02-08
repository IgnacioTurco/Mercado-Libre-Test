from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class index:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.search_bar = (By.ID, 'cb1-edit')
        self.query_top = (By.CLASS_NAME, 'nav-search-btn')
        self.accept_cookie = (By. XPATH, '/html/body/div[2]/div[1]/div[2]/button[1]')

    def search_item(self, item):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.search_bar)).send_keys(item)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.query_top)).click()
    def delete_cookie(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.accept_cookie)).click()

