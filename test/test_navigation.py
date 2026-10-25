from urllib.parse import urlparse

import allure
from selenium.webdriver.support import expected_conditions as EC

from page_object.main_page import MainPage


@allure.feature("Навигация")
def test_scooter_logo_returns_to_homepage(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_order_button("top")

    with allure.step("Перейти на главную по логотипу Самоката"):
        main_page.click_scooter_logo()
        main_page.wait.until(EC.url_to_be(main_page.URL))

    assert driver.current_url == main_page.URL


@allure.feature("Навигация")
def test_yandex_logo_opens_dzen_in_new_window(driver):
    main_page = MainPage(driver)
    main_page.open()
    original_window = driver.current_window_handle

    with allure.step("Открыть логотип Яндекса в новой вкладке"):
        main_page.click_yandex_logo()
        main_page.wait.until(EC.new_window_is_opened([original_window]))

    new_window = next(
        handle for handle in driver.window_handles if handle != original_window
    )
    driver.switch_to.window(new_window)
    main_page.wait.until(lambda browser: browser.current_url != "about:blank")

    assert urlparse(driver.current_url).hostname == "dzen.ru"
