from selenium.webdriver.common.by import By


FAQ_ITEMS = (By.CSS_SELECTOR, ".accordion__item")
COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")
ORDER_BUTTONS = (By.XPATH, '//button[normalize-space()="Заказать"]')
SCOOTER_LOGO = (By.XPATH, '//a[.//img[@alt="Scooter"]]')
YANDEX_LOGO = (By.XPATH, '//a[.//img[@alt="Yandex"]]')


def faq_question(question: str) -> tuple[str, str]:
    return (
        By.XPATH,
        f'//div[@role="button" and normalize-space()="{question}"]',
    )


def faq_answer_panel(panel_id: str) -> tuple[str, str]:
    return By.ID, panel_id
