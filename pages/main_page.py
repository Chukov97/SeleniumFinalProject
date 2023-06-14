from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):
    # Locators
    accept_cookies = '//button[@class="e4uhfkv0 css-1jfe691 e4mggex0"]'
    select_smartphone = '//*[@id="__next"]/div/main/div[1]/div[1]/div/div[2]/div/div[2]/div/a[2]/div[2]/span[1]'
    word = '//h1[@class="e1e4gwta0 eml1k9j0 app-catalog-yhwyfr e1gjr6xo0"]'

    # Getters
    def get_accept_cookies(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accept_cookies)))

    def get_select_smartphone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_smartphone)))

    def get_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word)))

    # Actions
    def click_accept_cookies(self):
        self.get_accept_cookies().click()
        print('Click cookies')

    def click_select_smartphone(self):
        self.get_select_smartphone().click()
        print('Click select smartphone')

    # Methods
    def link_to_smartphone_page(self):
        with allure.step('Link to smartphone page'):
            Logger.add_start_step(method='link_to_smartphone_page')
            self.get_current_url()
            self.click_accept_cookies()
            self.click_select_smartphone()
            print(self.get_word().text)
            self.assert_word(self.get_word(), 'Смартфоны')
            Logger.add_end_step(url=self.driver.current_url, method='link_to_smartphone_page')
