from selenium.webdriver.support import expected_conditions as EC

from constants import MAIN_PAGE_URL, ORDER_PAGE_URL
from page_object.base_page import BasePage
from locators.main_page_locators import (
    COOKIE_ACCEPT_BUTTON,
    FAQ_ITEMS,
    ORDER_BUTTONS,
    SCOOTER_LOGO,
    YANDEX_LOGO,
    faq_answer_panel,
    faq_question,
)


class MainPage(BasePage):
    def open(self) -> None:
        self.open_url(MAIN_PAGE_URL)
        self.wait_until(EC.presence_of_element_located(FAQ_ITEMS))
        if self.find_elements(COOKIE_ACCEPT_BUTTON):
            self.wait_until(
                EC.element_to_be_clickable(COOKIE_ACCEPT_BUTTON)
            ).click()

    def click_order_button(self, location: str) -> None:
        button_indexes = {"top": 0, "bottom": 1}
        if location not in button_indexes:
            raise ValueError(f"Unknown order button location: {location}")

        buttons = self.wait_for_elements_count(ORDER_BUTTONS, 2)
        buttons[button_indexes[location]].click()
        self.wait_for_url(ORDER_PAGE_URL)

    def get_faq_answer(self, question: str) -> str:
        question_button = self.wait_until(
            EC.element_to_be_clickable(faq_question(question))
        )
        question_button.click()
        self.wait_until(
            lambda _: question_button.get_attribute("aria-expanded") == "true"
        )

        panel_id = question_button.get_attribute("aria-controls")
        answer = self.wait_until(
            EC.visibility_of_element_located(faq_answer_panel(panel_id))
        )
        return answer.text

    def click_scooter_logo(self) -> None:
        self.wait_until(EC.element_to_be_clickable(SCOOTER_LOGO)).click()

    def open_yandex_logo_in_new_window(self) -> str:
        original_window = self.current_window_handle
        self.wait_until(EC.element_to_be_clickable(YANDEX_LOGO)).click()
        self.wait_for_new_window([original_window])

        new_window = next(
            handle
            for handle in self.window_handles
            if handle != original_window
        )
        self.switch_to_window(new_window)
        self.wait_until(lambda _: self.current_url != "about:blank")
        return self.current_url
