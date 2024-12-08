import allure
import time
from locators.internet.tags import DailyTagPages101Locators, TagPagelocators, LocatorsForOtherPages
from locators.internet.tags import PopupFillTheAddress, PopupSuccess
from pages.base_page import BasePage
from selenium.webdriver import ActionChains
from locators.internet.main import MainClass


class OneHundredMainPage(BasePage):
    @allure.step("Открыть страницу Тарифы")
    def close_form(self):
        self.element_is_visible(MainClass.CHOOSE_THE_FORM).click()

    @allure.step("Открыть страницу Тарифы")
    def open_rates(self):
        self.element_is_visible(DailyTagPages101Locators.CLICK_ON_THE_RATES).click()

    @allure.step("Выполнить проверку всех тегов страницы")
    def send_application_region_tag(self):
        with allure.step("Проверка TAG_INTERNET_AND_MOBILE"):
            self.element_is_visible(TagPagelocators.TAG_INTERNET_AND_MOBILE).click()
            self.execute_actions_after_rates_click()
            self.choose_connection_type()
            self.voronezh_assert_text()
            time.sleep(60)
        with allure.step("Проверка TAG_INTERNET_TV_MOBILE"):
            self.element_is_visible(TagPagelocators.TAG_INTERNET_TV_MOBILE).click()
            self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS).click()
            self.choose_connection_type()
            self.voronezh_assert_text()
            time.sleep(60)
        tags_to_check = [
            TagPagelocators.TAG_HOME_INTERNET,
            # TagPagelocators.TAG_INTERNET_TV,
            # TagPagelocators.TAG_CHEAP_INTERNET,
            # TagPagelocators.TAG_100_MB,
            # TagPagelocators.TAG_300_MB,
            # TagPagelocators.TAG_500_MB,
            # TagPagelocators.TAG_ONLINE_CINEMA
        ]
        for tag in tags_to_check:
            with allure.step(f"Проверка {tag}"):
                self.element_is_visible(tag).click()
                self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS_SECOND).click()
                self.choose_connection_type()
                self.voronezh_assert_text()
                time.sleep(60)

    @allure.step("Заполнить адрес для города Воронеж")
    def execute_actions_after_rates_click(self):
        self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS).click()
        self.element_is_visible(PopupFillTheAddress.POP_UP_FILLED_THE_STREET).send_keys('Полевая ул')
        self.element_is_visible(PopupFillTheAddress.CLICK_ON_THE_STREET).click()
        self.element_is_visible(PopupFillTheAddress.POP_UP_FILLED_THE_HOUSE).send_keys('5')
        self.element_is_visible(PopupFillTheAddress.CLICK_ON_THE_HOUSE).click()

    @allure.step("Заполнить попап и выбрать тип соединения")
    def choose_connection_type(self):
        self.element_is_visible(PopupFillTheAddress.POP_UP_CONNECTION_TYPE).click()
        self.element_is_visible(PopupFillTheAddress.POP_UP_SELECT_CONNECTION_TYPE).click()
        self.element_is_visible(PopupFillTheAddress.POP_UP_BUTTON_CHECK).click()

    @allure.step("Проверить текст попапа и отправить заявку")
    def voronezh_assert_text(self):
        text_in_pop_up = self.element_is_present(PopupSuccess.POP_UP_TEXT).text
        if text_in_pop_up == ("Отлично! Подключение возможно. Введите номер "
                              "телефона, оператор перезвонит вам в ближайшее "
                              "время."):
            self.element_is_visible(PopupSuccess.POP_UP_SUCCESS_NUMBER).send_keys('3333333333')
            self.close_form()
            self.element_is_visible(PopupSuccess.POP_UP_SUCCESS_BUTTON).click()
            self.element_is_visible(PopupSuccess.CLOSE_SUCCESS_WINDOW).click()
            print("Провайдер доступен в этом доме")
        elif text_in_pop_up != ("Отлично! Подключение возможно. Введите номер "
                                "телефона, оператор перезвонит вам в ближайшее "
                                "время."):
            self.element_is_visible(PopupSuccess.POP_UP_NOT_SUCCESS_NUMBER).send_keys('3333333333')
            self.element_is_visible(PopupSuccess.POP_UP_SUCCESS_BUTTON).click()
            self.element_is_visible(PopupSuccess.CLOSE_THE_WINDOW).click()
            print("Провайдер недоступен в этом доме, отправлена заявки на другие")
        self.driver.back()

    @allure.step("Заполнить адрес для города Москва")
    def send_application_provider(self):
        self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS).click()
        self.element_is_visible(LocatorsForOtherPages.POP_UP_FILLED_THE_STREET).send_keys('Арбат ул')
        self.element_is_visible(LocatorsForOtherPages.CLICK_ON_THE_STREET).click()
        self.element_is_visible(LocatorsForOtherPages.POP_UP_FILLED_THE_HOUSE).send_keys('10')
        self.element_is_visible(LocatorsForOtherPages.CLICK_ON_THE_HOUSE).click()

    @allure.step("Выполнить проверку тегов страницы")
    def new_application_provider(self):
        self.send_application_provider()
        self.choose_connection_type()
        self.moscow_assert_text()
        time.sleep(60)
        with allure.step("Проверка TAG_INTERNET_TV_MOBILE"):
            self.element_is_visible(TagPagelocators.TAG_INTERNET_TV_MOBILE).click()
            self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS).click()
            self.choose_connection_type()
            self.moscow_assert_text()
            time.sleep(60)
        # new_new_tags = [TagPagelocators.TAG_HOME_INTERNET]
        #                 # TagPagelocators.TAG_INTERNET_TV,
        #                 # TagPagelocators.TAG_CHEAP_INTERNET,
        #                 # TagPagelocators.TAG_ONLINE_CINEMA]
        # for new_tag in new_new_tags:
        #     with allure.step(f"Проверка {new_tag}"):
        #         self.element_is_visible(new_tag).click()
        #         self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS_SECOND).click()
        #         self.choose_connection_type()
        #         self.moscow_assert_text()
                # time.sleep(60)

    @allure.step("Проверить текст попапа и отправить заявку для города Москва")
    def moscow_assert_text(self):
        text_in_pop_up = self.element_is_present(PopupSuccess.POP_UP_TEXT).text
        if text_in_pop_up == ("Отлично! Подключение возможно. Введите номер "
                              "телефона, оператор перезвонит вам в ближайшее "
                              "время."):
            self.element_is_visible(PopupSuccess.POP_UP_SUCCESS_NUMBER).send_keys('3333333333')
            self.element_is_visible(PopupSuccess.POP_UP_SUCCESS_BUTTON).click()
            self.element_is_visible(PopupSuccess.CLOSE_SUCCESS_WINDOW).click()
            print("Провайдер доступен в этом доме")
        elif text_in_pop_up != ("Отлично! Подключение возможно. Введите номер "
                                "телефона, оператор перезвонит вам в ближайшее "
                                "время."):
            self.element_is_visible(LocatorsForOtherPages.POP_UP_NOT_SUCCESS_NUMBER).send_keys('3333333333')
            self.element_is_visible(PopupSuccess.POP_UP_SUCCESS_BUTTON).click()
            self.element_is_visible(LocatorsForOtherPages.CLOSE_THE_WINDOW).click()
            print("Провайдер недоступен в этом доме, отправлена заявки на другие")

    @allure.step("Заполнить адрес для города Екатеринбург")
    def send_application_provider_ekb(self):
        self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS).click()
        self.element_is_visible(LocatorsForOtherPages.POP_UP_FILLED_THE_STREET).send_keys('Гастелло ул')
        self.element_is_visible(LocatorsForOtherPages.CLICK_ON_THE_STREET).click()
        self.element_is_visible(LocatorsForOtherPages.POP_UP_FILLED_THE_HOUSE).send_keys('32')
        self.element_is_visible(LocatorsForOtherPages.CLICK_ON_THE_HOUSE).click()

    @allure.step("Выполнить проверку тегов страницы")
    def new_application_provider_ekb(self):
        self.send_application_provider_ekb()
        self.choose_connection_type()
        self.moscow_assert_text()
        time.sleep(60)
        with allure.step("Проверка TAG_INTERNET_TV_MOBILE"):
            self.element_is_visible(TagPagelocators.TAG_INTERNET_TV_MOBILE).click()
            self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS).click()
            self.choose_connection_type()
            self.moscow_assert_text()
            time.sleep(60)

