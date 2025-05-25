import allure
from conftest import driver
from pages.main_page import MainPage


class TestLogo:

    @allure.title('Проверка перехода на главную страницу сервиса при нажатии на логотип "Самокат"')
    def test_cross_to_main_page_on_click_logo_scooter_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_button_order_in_header()
        main_page.click_on_button_order_in_header()
        main_page.wait_visibility_of_logo_scooter()
        main_page.click_on_logo_scooter()
        main_page.wait_visibility_of_main_header()
        assert main_page.check_displaying_of_main_header()

    @allure.title('Проверка перехода на главную страницу Дзена при нажатии на логотип "Яндекс"')
    def test_cross_to_dzen_on_click_logo_yandex_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_logo_yandex()
        main_page.click_on_logo_yandex()
        main_page.switch_to_next_tab()
        assert 'Дзен' in main_page.get_page_title()

# pytest tests/test_logo_click.py
