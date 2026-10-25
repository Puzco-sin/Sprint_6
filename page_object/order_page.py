from datetime import date, timedelta

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from page_object.base_page import BasePage


class OrderPage(BasePage):
    FIRST_NAME = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
    ADDRESS = (
        By.CSS_SELECTOR,
        'input[placeholder="* Адрес: куда привезти заказ"]',
    )
    METRO_STATION = (By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]')
    PHONE = (
        By.CSS_SELECTOR,
        'input[placeholder="* Телефон: на него позвонит курьер"]',
    )
    DELIVERY_DATE = (
        By.CSS_SELECTOR,
        'input[placeholder="* Когда привезти самокат"]',
    )
    RENTAL_PERIOD = (By.CSS_SELECTOR, ".Dropdown-control")
    ORDER_BUTTONS = (By.XPATH, '//button[normalize-space()="Заказать"]')
    CONFIRMATION_TITLE = (
        By.XPATH,
        '//div[contains(@class,"ModalHeader") and contains(.,"Хотите оформить заказ?")]',
    )
    SUCCESS_TITLE = (
        By.XPATH,
        '//div[contains(@class,"ModalHeader") and contains(.,"Заказ оформлен")]',
    )

    def fill_personal_details(self, order_data: dict[str, str]) -> None:
        fields = (
            (self.FIRST_NAME, order_data["first_name"]),
            (self.LAST_NAME, order_data["last_name"]),
            (self.ADDRESS, order_data["address"]),
            (self.PHONE, order_data["phone"]),
        )
        for locator, value in fields:
            self.wait.until(EC.visibility_of_element_located(locator)).send_keys(
                value
            )

        metro_input = self.wait.until(
            EC.visibility_of_element_located(self.METRO_STATION)
        )
        metro_input.send_keys(order_data["metro_station"])
        station_option = (
            By.XPATH,
            f'//button[normalize-space()="{order_data["metro_station"]}"]',
        )
        self.wait.until(EC.element_to_be_clickable(station_option)).click()
        self.driver.find_element(
            By.XPATH, '//button[normalize-space()="Далее"]'
        ).click()
        self.wait.until(EC.visibility_of_element_located(self.DELIVERY_DATE))

    def fill_rental_details(self, order_data: dict[str, str]) -> None:
        delivery_date = self.wait.until(
            EC.visibility_of_element_located(self.DELIVERY_DATE)
        )
        requested_date = (date.today() + timedelta(days=1)).strftime("%d.%m.%Y")
        delivery_date.send_keys(requested_date, Keys.ESCAPE)
        self.wait.until(
            lambda _: delivery_date.get_attribute("value") == requested_date
        )
        self.wait.until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".react-datepicker"))
        )

        self.wait.until(
            EC.element_to_be_clickable(self.RENTAL_PERIOD)
        ).click()
        rental_period_option = (
            By.XPATH,
            '//div[contains(@class,"Dropdown-option") '
            f'and normalize-space()="{order_data["rental_period"]}"]',
        )
        self.wait.until(
            EC.element_to_be_clickable(rental_period_option)
        ).click()

        color = self.driver.find_element(By.ID, order_data["color"])
        color.click()
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]'
        ).send_keys(order_data["comment"])

    def submit_order(self) -> str:
        buttons = self.wait.until(
            lambda driver: (
                found
                if len(found := driver.find_elements(*self.ORDER_BUTTONS)) >= 2
                else False
            )
        )
        buttons[-1].click()
        self.wait.until(EC.visibility_of_element_located(self.CONFIRMATION_TITLE))
        self.driver.find_element(
            By.XPATH, '//button[normalize-space()="Да"]'
        ).click()
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_TITLE)
        ).text

    def is_order_form_open(self) -> bool:
        return self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        ).is_displayed()
