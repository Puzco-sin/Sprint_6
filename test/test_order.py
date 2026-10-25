import allure
import pytest

from page_object.main_page import MainPage
from page_object.order_page import OrderPage


ORDER_CASES = [
    pytest.param(
        {
            "first_name": "Алексей",
            "last_name": "Иванов",
            "address": "Москва, улица Тестовая, 1",
            "metro_station": "Сокольники",
            "phone": "+79990000001",
            "rental_period": "сутки",
            "color": "black",
            "comment": "Позвонить за 10 минут.",
        },
        "top",
        id="header-button",
    ),
    pytest.param(
        {
            "first_name": "Анна",
            "last_name": "Петрова",
            "address": "Москва, улица Учебная, 2",
            "metro_station": "Сокольники",
            "phone": "+79990000002",
            "rental_period": "двое суток",
            "color": "grey",
            "comment": "Оставить у двери.",
        },
        "bottom",
        id="footer-button",
    ),
]


@allure.feature("Заказ самоката")
@pytest.mark.parametrize(("order_data", "entry_button"), ORDER_CASES)
def test_order_can_be_created_from_each_entry_point(
    driver, order_data, entry_button
):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    with allure.step("Открыть главную страницу"):
        main_page.open()
    with allure.step(f"Начать заказ через кнопку «Заказать» ({entry_button})"):
        main_page.click_order_button(entry_button)
        assert order_page.is_order_form_open()
    with allure.step("Заполнить данные заказчика"):
        order_page.fill_personal_details(order_data)
    with allure.step("Заполнить параметры аренды и отправить заказ"):
        order_page.fill_rental_details(order_data)
        success_message = order_page.submit_order()

    assert "Заказ оформлен" in success_message
