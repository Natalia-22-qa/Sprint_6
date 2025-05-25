import allure
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    # методы для тестов проверки переключения страниц (test_logo_click.py)
    @allure.step('Подождать прогрузки кнопки "Заказать" в шапке')
    def wait_visibility_of_button_order_in_header(self):
        self.wait_visibility_of_element(BasePageLocators.button_order_in_header)

    @allure.step('Кликнуть по кнопке "Заказать" в шапке')
    def click_on_button_order_in_header(self):
        self.click_on_element(BasePageLocators.button_order_in_header)

    @allure.step('Подождать прогрузки части логотипа с надписью "Самокат" в шапке')
    def wait_visibility_of_logo_scooter(self):
        self.wait_visibility_of_element(BasePageLocators.logo_scooter)

    @allure.step('Кликнуть по части логотипа с надписью "Самокат" в шапке')
    def click_on_logo_scooter(self):
        self.click_on_element(BasePageLocators.logo_scooter)

    @allure.step('Подождать прогрузки части логотипа с надписью "Яндекс" в шапке')
    def wait_visibility_of_logo_yandex(self):
        self.wait_visibility_of_element(BasePageLocators.logo_yandex)

    @allure.step('Кликнуть по части логотипа с надписью "Яндекс" в шапке')
    def click_on_logo_yandex(self):
        self.click_on_element(BasePageLocators.logo_yandex)

    @allure.step('Подождать прогрузки отображения заголовка главной страницы')
    def wait_visibility_of_main_header(self):
        self.wait_visibility_of_element(MainPageLocators.main_header)

    @allure.step('Проверить отображение заголовка главной страницы')
    def check_displaying_of_main_header(self):
        return self.check_displaying_of_element(MainPageLocators.main_header)

    # методы для тестов проверки блока "Вопросы о важном" (test_main_page.py)
    @allure.step('Прокрутить до блока "Вопросы о важном"')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.faq_section)

    @allure.step('Подождать прогрузки нужного вопроса в "Вопросы о важном"')
    def wait_visibility_of_faq_question(self, data):
        self.wait_visibility_of_element(MainPageLocators.faq_questions[data])

    @allure.step('Кликнуть на вопрос в "Вопросы о важном"')
    def click_on_faq_question(self, data):
        self.click_on_element(MainPageLocators.faq_questions[data])

    @allure.step('Подождать прогрузки нужного ответа в "Вопросы о важном"')
    def wait_visibility_of_faq_answer(self, data):
        self.wait_visibility_of_element(MainPageLocators.faq_answers[data])

    @allure.step('Получить текст нужного номера ответа в "Вопросы о важном"')
    def get_text_of_faq_answer(self, data):
        return self.get_text_on_element(MainPageLocators.faq_answers[data])
