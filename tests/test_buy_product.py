import time
import allure
from pages.cart_page import CartPage
from pages.iphone_page import IphonePage
from pages.main_page import MainPage
from pages.ordering_page import OrderingPage
from pages.smartphone_page import SmartphonePage


@allure.description('Test buy product')
def test_buy_product_1(driver):
    print('Start test 1')

    mp = MainPage(driver)
    mp.link_to_smartphone_page()

    sp = SmartphonePage(driver)
    sp.select_iphone()

    ip = IphonePage(driver)
    ip.add_to_cart_page()

    cp = CartPage(driver)
    cp.to_ordering()

    op = OrderingPage(driver)
    op.create_order()

    print('Finish Test 1')
    time.sleep(10)
