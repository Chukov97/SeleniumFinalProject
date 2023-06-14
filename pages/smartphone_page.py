import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class SmartphonePage(Base):
    # Locators
    checkbox_apple = '//div[@data-meta-value="APPLE"]'
    select_iphone_1 = '//a[@title="Смартфон Apple iPhone 14 Pro 128Gb,  A2889,  темно-фиолетовый"]'
    price_iphone_1 = '//*[@id="__next"]/div/main/section/div[2]/div/div/section/div[2]/div[2]/div[1]/div/div[7]/div[1]/div[2]/span/span/span[1]'

    # Getters
    def get_checkbox_apple(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_apple)))

    def get_select_iphone_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_iphone_1)))

    def get_price_iphone_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_iphone_1)))

    # Actions
    def click_checkbox_apple(self):
        self.get_checkbox_apple().click()
        print('Click cookies')

    def click_select_iphone_1(self):
        self.get_select_iphone_1().click()
        print('Add to cart')

    # Methods
    def select_iphone(self):
        with allure.step('Select iphone'):
            Logger.add_start_step(method='select_iphone')
            self.get_current_url()
            self.click_checkbox_apple()
            self.driver.refresh()
            self.click_select_iphone_1()
            Logger.add_end_step(url=self.driver.current_url, method='select_iphone')
