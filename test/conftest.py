import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from page_object.main_page import MainPage
from page_object.order_page import OrderPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("-headless")
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    browser = webdriver.Firefox(options=options)
    yield browser
    browser.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def order_page(driver):
    return OrderPage(driver)
