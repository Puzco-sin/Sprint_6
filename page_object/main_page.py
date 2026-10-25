from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from page_object.base_page import BasePage


class MainPage(BasePage):
    URL = "https://qa-scooter.education-services.ru/"
    ORDER_BUTTONS = (By.XPATH, '//button[normalize-space()="Заказать"]')
    SCOOTER_LOGO = (By.XPATH, '//a[.//img[@alt="Scooter"]]')
    YANDEX_LOGO = (By.XPATH, '//a[.//img[@alt="Yandex"]]')

    def open(self) -> None:
        self.driver.get(self.URL)
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".accordion__item"))
        )
        cookie_button = (By.ID, "rcc-confirm-button")
        if self.driver.find_elements(*cookie_button):
            self.wait.until(EC.element_to_be_clickable(cookie_button)).click()

    def click_order_button(self, location: str) -> None:
        button_indexes = {"top": 0, "bottom": 1}
        if location not in button_indexes:
            raise ValueError(f"Unknown order button location: {location}")

        buttons = self.wait.until(
            lambda driver: (
                found
                if len(found := driver.find_elements(*self.ORDER_BUTTONS)) == 2
                else False
            )
        )
        buttons[button_indexes[location]].click()

    def get_faq_answer(self, question: str) -> str:
        question_locator = (
            By.XPATH,
            f'//div[@role="button" and normalize-space()="{question}"]',
        )
        question_button = self.wait.until(
            EC.element_to_be_clickable(question_locator)
        )
        question_button.click()
        self.wait.until(
            lambda _: question_button.get_attribute("aria-expanded") == "true"
        )

        panel_id = question_button.get_attribute("aria-controls")
        answer = self.wait.until(
            EC.visibility_of_element_located((By.ID, panel_id))
        )
        return answer.text

    def click_scooter_logo(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.SCOOTER_LOGO)).click()

    def click_yandex_logo(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.YANDEX_LOGO)).click()
