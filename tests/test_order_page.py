import allure
import pytest
from conftest import driver
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage
from data import TestData


class TestOrderPageOrder:

    @allure.title('Проверка позитивного сценария оформления заказа')
    @allure.description('Тестирование всего пути оформления заказа из двух точек входа')
    @pytest.mark.parametrize('button, test_data', [(BasePageLocators.button_order_in_header, TestData.test_user_1),
                                                   (MainPageLocators.button_order_main_page, TestData.test_user_2)])
    def test_order_success(self, driver, button, test_data):
        order_page = OrderPage(driver)
        order_page.scroll_to_element(button)
        order_page.wait_visibility_of_element(button)
        order_page.click_on_element(button)
        order_page.data_entry_first_form(test_data)
        order_page.data_entry_second_form(test_data)
        assert order_page.check_displaying_of_title_order_formed()

# pytest tests/test_order_page.py
