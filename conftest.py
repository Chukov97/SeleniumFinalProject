import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    url = 'https://www.citilink.ru'
    driver_path = r'C:\Users\Licard\Desktop\Develop\resource\chromedriver.exe'
    chrome_service = Service(executable_path=driver_path)
    chrome_options = Options()
    chrome_options.page_load_strategy = 'eager'
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()
