import pytest


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
