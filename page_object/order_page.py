from datetime import date, timedelta

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from page_object.base_page import BasePage
from locators.order_page_locators import (
    ADDRESS,
    COLOR_CHECKBOXES,
    CONFIRMATION_TITLE,
    CONFIRM_ORDER_BUTTON,
    COURIER_COMMENT,
    DATE_PICKER,
    DELIVERY_DATE,
    FIRST_NAME,
    LAST_NAME,
    METRO_STATION,
    METRO_STATION_OPTIONS,
    NEXT_BUTTON,
    ORDER_BUTTONS,
    PHONE,
    RENTAL_PERIOD,
    RENTAL_PERIOD_OPTIONS,
    SUCCESS_TITLE,
)


class OrderPage(BasePage):
    def fill_personal_details(self, order_data: dict[str, str]) -> None:
        fields = (
            (FIRST_NAME, order_data["first_name"]),
            (LAST_NAME, order_data["last_name"]),
            (ADDRESS, order_data["address"]),
            (PHONE, order_data["phone"]),
        )
        for locator, value in fields:
            self.wait_until(EC.visibility_of_element_located(locator)).send_keys(value)

        metro_input = self.wait_until(
            EC.visibility_of_element_located(METRO_STATION)
        )
        metro_input.send_keys(order_data["metro_station"])
        station_option = self.wait_for_matching_element(
            METRO_STATION_OPTIONS, order_data["metro_station"]
        )
        station_option.click()
        self.find_element(NEXT_BUTTON).click()
        self.wait_until(EC.visibility_of_element_located(DELIVERY_DATE))

    def fill_rental_details(self, order_data: dict[str, str]) -> None:
        delivery_date = self.wait_until(
            EC.visibility_of_element_located(DELIVERY_DATE)
        )
        requested_date = (date.today() + timedelta(days=1)).strftime("%d.%m.%Y")
        delivery_date.send_keys(requested_date, Keys.ESCAPE)
        self.wait_until(
            lambda _: delivery_date.get_attribute("value") == requested_date
        )
        self.wait_until(EC.invisibility_of_element_located(DATE_PICKER))

        self.wait_until(EC.element_to_be_clickable(RENTAL_PERIOD)).click()
        rental_period_option = self.wait_for_matching_element(
            RENTAL_PERIOD_OPTIONS, order_data["rental_period"]
        )
        rental_period_option.click()

        color = self.find_element(COLOR_CHECKBOXES[order_data["color"]])
        color.click()
        self.find_element(COURIER_COMMENT).send_keys(order_data["comment"])

    def submit_order(self) -> str:
        buttons = self.wait_until(
            lambda _: (
                found
                if len(found := self.find_elements(ORDER_BUTTONS)) >= 2
                else False
            )
        )
        buttons[-1].click()
        self.wait_until(EC.visibility_of_element_located(CONFIRMATION_TITLE))
        self.find_element(CONFIRM_ORDER_BUTTON).click()
        return self.wait_until(EC.visibility_of_element_located(SUCCESS_TITLE)).text
