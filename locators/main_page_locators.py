from selenium.webdriver.common.by import By


class MainPageLocators:
    main_header = (By.XPATH, ".//div[contains(@class, 'Home_Header__iJKdX')]")
    # кнопка "Заказать" на главной странице
    button_order_main_page = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[text() = 'Заказать']")
    # заголовок ресурса "Дзен"
    title_dzen = (By.TAG_NAME, 'title')
    # раздел "Вопросы о важном"
    faq_section = (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]")
    faq_questions = {
        1: (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]//div[@id = 'accordion__heading-0']"),
        2: (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]//div[@id = 'accordion__heading-1']"),
        3: (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]//div[@id = 'accordion__heading-2']"),
        4: (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]//div[@id = 'accordion__heading-3']"),
        5: (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]//div[@id = 'accordion__heading-4']"),
        6: (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]//div[@id = 'accordion__heading-5']"),
        7: (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]//div[@id = 'accordion__heading-6']"),
        8: (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]//div[@id = 'accordion__heading-7']")
    }
    faq_answers = {
        1: (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]//div[@id = 'accordion__panel-0']"),
        2: (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]//div[@id = 'accordion__panel-1']"),
        3: (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]//div[@id = 'accordion__panel-2']"),
        4: (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]//div[@id = 'accordion__panel-3']"),
        5: (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]//div[@id = 'accordion__panel-4']"),
        6: (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]//div[@id = 'accordion__panel-5']"),
        7: (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]//div[@id = 'accordion__panel-6']"),
        8: (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]//div[@id = 'accordion__panel-7']")
    }
