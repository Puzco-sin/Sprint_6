from urllib.parse import urlparse

import allure

from constants import DZEN_URL, MAIN_PAGE_URL


@allure.feature("Навигация")
class TestNavigation:
    def test_scooter_logo_returns_to_homepage(self, main_page):
        main_page.open()
        main_page.click_order_button("top")

        with allure.step("Перейти на главную по логотипу Самоката"):
            main_page.click_scooter_logo()
            main_page.wait_for_url(MAIN_PAGE_URL)

        assert main_page.current_url == MAIN_PAGE_URL


    def test_yandex_logo_opens_dzen_in_new_window(self, main_page):
        main_page.open()

        with allure.step("Открыть логотип Яндекса в новой вкладке"):
            destination_url = main_page.open_yandex_logo_in_new_window()

        assert (
            urlparse(destination_url).hostname
            == urlparse(DZEN_URL).hostname
        )
