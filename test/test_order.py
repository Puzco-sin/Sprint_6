import allure
import pytest

from test_data.order_data import ORDER_CASES


@allure.feature("Заказ самоката")
class TestOrder:
    @pytest.mark.parametrize(("order_data", "entry_button"), ORDER_CASES)
    def test_order_can_be_created_from_each_entry_point(
        self, main_page, order_page, order_data, entry_button
    ):
        with allure.step("Открыть главную страницу"):
            main_page.open()
        with allure.step(f"Начать заказ через кнопку «Заказать» ({entry_button})"):
            main_page.click_order_button(entry_button)
        with allure.step("Заполнить данные заказчика"):
            order_page.fill_personal_details(order_data)
        with allure.step("Заполнить параметры аренды и отправить заказ"):
            order_page.fill_rental_details(order_data)
            success_message = order_page.submit_order()

        assert "Заказ оформлен" in success_message
