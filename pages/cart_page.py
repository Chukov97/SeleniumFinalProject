from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger
import allure


class CartPage(Base):
    # Locators
    checkbox_warranty_extension = '//*[@id="__next"]/div/main/div[1]/div[2]/section/div[1]/div/div/div/div[6]/div[2]/div/div[2]/div/div[1]'
    price_phone = '//div[@class="css-144xb02 eakadi60"]'
    price_warranty_extension = '//*[@id="__next"]/div/main/div[1]/div[2]/section/div[1]/div/div/div/div[6]/div[2]/div/div[2]/div/div[1]/div[3]/span/span/span[1]'
    total_price = '//span[@class="e1j9birj0 e106ikdt0 css-zmmgir e1gjr6xo0"]'
    ordering = '//button[@class="e4uhfkv0 css-1ls3bkl e4mggex0"]'

    # Getters
    def get_checkbox_warranty_extension(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_warranty_extension)))

    def get_price_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_phone)))

    def get_price_warranty_extension(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_warranty_extension)))

    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_price)))

    def get_ordering(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ordering)))

    # Actions
    def click_checkbox_warranty_extension(self):
        self.get_checkbox_warranty_extension().click()
        print('Click checkbox warranty extension')

    def click_ordering(self):
        self.get_ordering().click()
        print('Click ordering button')

    # Methods
    def to_ordering(self):
        with allure.step('To ordering'):
            Logger.add_start_step(method='to_ordering')
            self.get_current_url()
            self.click_checkbox_warranty_extension()
            self.click_ordering()
            Logger.add_end_step(url=self.driver.current_url, method='to_ordering')
