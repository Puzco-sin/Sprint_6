# Автотесты сервиса «Яндекс.Самокат»

## Установка

```bash
python3 -m pip install -r requirements.txt
```

Для запуска Selenium-тестов необходим Mozilla Firefox. Selenium Manager автоматически
подбирает драйвер браузера.

## Что проверяют тесты

- Все 8 ответов раздела «Вопросы о важном».
- Оформление заказа с двумя наборами данных через верхнюю и нижнюю кнопки «Заказать».
- Переход на главную страницу по логотипу Самоката и открытие Дзена по логотипу Яндекса.

## Запуск тестов

```bash
python3 -m pytest test
```

## Allure-отчёт

```bash
python3 -m pytest test --alluredir=allure-results
allure serve allure-results
```

Для просмотра отчёта дополнительно установите Allure Commandline.
