from selenium.webdriver.common.by import By


FIRST_NAME = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
LAST_NAME = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
ADDRESS = (
    By.CSS_SELECTOR,
    'input[placeholder="* Адрес: куда привезти заказ"]',
)
METRO_STATION = (By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]')
METRO_STATION_OPTIONS = (By.CSS_SELECTOR, ".select-search__option")
PHONE = (
    By.CSS_SELECTOR,
    'input[placeholder="* Телефон: на него позвонит курьер"]',
)
NEXT_BUTTON = (By.XPATH, '//button[normalize-space()="Далее"]')
DELIVERY_DATE = (
    By.CSS_SELECTOR,
    'input[placeholder="* Когда привезти самокат"]',
)
DATE_PICKER = (By.CSS_SELECTOR, ".react-datepicker")
RENTAL_PERIOD = (By.CSS_SELECTOR, ".Dropdown-control")
RENTAL_PERIOD_OPTIONS = (By.CSS_SELECTOR, ".Dropdown-option")
COLOR_CHECKBOXES = {
    "black": (By.ID, "black"),
    "grey": (By.ID, "grey"),
}
COURIER_COMMENT = (
    By.CSS_SELECTOR,
    'input[placeholder="Комментарий для курьера"]',
)
CONFIRMATION_TITLE = (
    By.XPATH,
    '//div[contains(@class,"ModalHeader") and contains(.,"Хотите оформить заказ?")]',
)
CONFIRM_ORDER_BUTTON = (By.XPATH, '//button[normalize-space()="Да"]')
SUCCESS_TITLE = (
    By.XPATH,
    '//div[contains(@class,"ModalHeader") and contains(.,"Заказ оформлен")]',
)
ORDER_BUTTONS = (By.XPATH, '//button[normalize-space()="Заказать"]')
