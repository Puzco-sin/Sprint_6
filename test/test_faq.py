import allure
import pytest

from test_data.faq_data import FAQ_ITEMS


@allure.feature("Вопросы о важном")
class TestFAQ:
    @pytest.mark.parametrize(
        ("question", "expected_answer"),
        FAQ_ITEMS,
        ids=[question for question, _ in FAQ_ITEMS],
    )
    def test_faq_question_opens_its_answer(
        self, main_page, question, expected_answer
    ):
        with allure.step("Открыть главную страницу"):
            main_page.open()

        with allure.step(f"Открыть ответ на вопрос «{question}»"):
            actual_answer = main_page.get_faq_answer(question)

        assert actual_answer == expected_answer
