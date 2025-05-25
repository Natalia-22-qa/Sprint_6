import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнить первую часть формы заказа и нажать кнопку "Далее"')
    def data_entry_first_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.name)
        self.click_on_element(OrderPageLocators.name)
        self.send_keys_to_input(OrderPageLocators.name, test_data[0])
        self.click_on_element(OrderPageLocators.lastname)
        self.send_keys_to_input(OrderPageLocators.lastname, test_data[1])
        self.click_on_element(OrderPageLocators.address)
        self.send_keys_to_input(OrderPageLocators.address, test_data[2])
        self.click_on_element(OrderPageLocators.metro)
        self.send_keys_to_input(OrderPageLocators.metro, test_data[3])
        self.click_on_element(OrderPageLocators.select_metro)
        self.click_on_element(OrderPageLocators.phone)
        self.send_keys_to_input(OrderPageLocators.phone, test_data[4])
        self.click_on_element(OrderPageLocators.button_next)

    @allure.step('Заполнить вторую часть формы заказа и нажать на кнопку подтверждения заказа')
    def data_entry_second_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.date)
        self.click_on_element(OrderPageLocators.date)
        self.send_keys_to_input(OrderPageLocators.date, test_data[5])
        self.wait_visibility_of_element(OrderPageLocators.calendar)
        self.wait_visibility_of_element(OrderPageLocators.day)
        self.click_on_element(OrderPageLocators.day)
        self.click_on_element(OrderPageLocators.field_rental_period)
        self.click_on_element(OrderPageLocators.select_rental_period)
        self.click_on_element(test_data[6])
        self.click_on_element(OrderPageLocators.comment)
        self.send_keys_to_input(OrderPageLocators.comment, test_data[7])
        self.click_on_element(OrderPageLocators.button_make_order)
        self.wait_visibility_of_element(OrderPageLocators.button_yes_confirm_order)
        self.click_on_element(OrderPageLocators.button_yes_confirm_order)

    @allure.step('Проверить отображение заголовка окна "Заказ оформлен"')
    def check_displaying_of_title_order_formed(self):
        return self.check_displaying_of_element(OrderPageLocators.title_order_formed)
