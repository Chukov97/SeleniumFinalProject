import datetime


class Base:

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url {get_url}')

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Значения равны')

    def assert_price(self, price, result):
        value_price = price.text
        assert value_price == result
        print('Цена соответсвует')

    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = f'screenshot-{now_date}.png'
        self.driver.save_screenshot(f'./screen/{name_screenshot}.png')
