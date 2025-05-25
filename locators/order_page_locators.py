from selenium.webdriver.common.by import By


class OrderPageLocators:
    # первая часть формы заказа
    name = (By.XPATH, ".//input[@placeholder = '* Имя']")
    lastname = (By.XPATH, ".//input[@placeholder = '* Фамилия']")
    address = (By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']")
    metro = (By.XPATH, ".//input[@placeholder = '* Станция метро']")
    select_metro = (By.XPATH, ".//li[@class = 'select-search__row']")
    phone = (By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']")
    button_next = (By.XPATH, ".//button[text() = 'Далее']")
    # вторая часть формы заказа
    date = (By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']")
    calendar = (By.XPATH, ".//div[@class = 'react-datepicker__month-container']")
    day = (By.XPATH, ".//div[contains(@class, 'react-datepicker__day') and @tabindex ='0']")
    field_rental_period = (By.XPATH, ".//div[text() = '* Срок аренды']")
    select_rental_period = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() = 'сутки']")
    checkbox_black_color = (By.XPATH, ".//input[@id = 'black']")
    checkbox_grey_color = (By.XPATH, ".//input[@id = 'grey']")
    comment = (By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']")
    button_make_order = (By.XPATH, ".//div[contains(@class, 'Order_Button')]/button[text() = 'Заказать']")
    button_yes_confirm_order = (By.XPATH, ".//button[text() = 'Да']")
    title_order_formed = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader') and text() = 'Заказ оформлен']")
