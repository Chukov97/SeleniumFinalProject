import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class OrderingPage(Base):
    # Locators
    first_name = '//input[@name="contact-form_firstName"]'
    last_name = '//input[@name="contact-form_lastName"]'
    phone_number = '//input[@name="contact-form_phone"]'
    delivery = '//label[@class="el7jmaq0 e1twwlg30 css-1ia32xb e1amf8g0"]'
    street = '//input[@name="street"]'
    select_street = '//div[@tabindex="0"]'
    house = '//input[@name="courier-delivery-new-address-form_house"]'

    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery)))

    def get_street(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.street)))

    def get_select_street(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_street)))

    def get_house(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.house)))

    # Actions
    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print('Input first name')

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('Input last name')

    def input_phone_number(self, phone_number):
        self.get_phone_number().send_keys(phone_number)
        print('Input phone number')

    def click_get_delivery(self):
        self.get_delivery().click()
        print('Click delivery')

    def input_street(self, street):
        self.get_street().send_keys(street)
        print('Input street')

    def click_street(self):
        self.get_select_street().click()
        print('Select street')

    def input_house(self, house):
        self.get_house().send_keys(house)
        print('Input house')

    # Methods
    def create_order(self):
        with allure.step('Create order'):
            Logger.add_start_step(method='create_order')
            self.get_current_url()
            self.input_first_name('Ivan')
            self.input_last_name('Ivanov')
            self.input_phone_number('79100000000')
            self.click_get_delivery()
            self.input_street('Бутлерова')
            self.get_select_street()
            self.input_house('55')
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='create_order')
