import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger

"""Страница товара IPhone"""


class IphonePage(Base):
    # Locators
    price = '//span[@class="e1j9birj0 e106ikdt0 app-catalog-1f8xctp e1gjr6xo0"]'
    name_of_product = '//h1[@class="e1ubbx7u0 eml1k9j0 app-catalog-tn2wxd e1gjr6xo0"]'
    add_to_cart = '//button[@class="e11w80q30 e4uhfkv0 app-catalog-1c1fy1q e4mggex0"]'
    go_to_cart = '//button[@class="e4uhfkv0 css-10je9jt e4mggex0"]'

    # Getters
    def get_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_name_of_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_of_product)))

    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))

    # Actions
    def click_add_to_cart(self):
        self.get_add_to_cart().click()
        print('Click add to cart')

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print('Go to cart')

    # Methods
    def add_to_cart_page(self):
        with allure.step('Add to cart page'):
            Logger.add_start_step(method='add_to_cart_page')
            self.get_current_url()
            self.assert_price(self.get_price(), '109 590')
            self.assert_word(self.get_name_of_product(), 'Смартфон Apple iPhone 14 Pro 128Gb, A2889, темно-фиолетовый')
            self.click_add_to_cart()
            self.click_go_to_cart()
            Logger.add_end_step(url=self.driver.current_url, method='add_to_cart_page')
