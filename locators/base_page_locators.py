from selenium.webdriver.common.by import By


class BasePageLocators:
    # кнопка "Заказать" в шапке сайта
    button_order_in_header = (By.XPATH, ".//div[@class = 'Header_Nav__AGCXC']/button[text() = 'Заказать']")
    # часть логотипа - "Самокат"
    logo_scooter = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter') and @href = '/']")
    # часть логотипа - "Яндекс"
    logo_yandex = (By.XPATH, ".//a[@href = '//yandex.ru' and contains(@class, 'Header_LogoYandex')]")
