import allure
import time
from locators.internet.main import MainClass
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Открыть страницу Тарифы")
    def close_form(self):
        self.element_is_visible(MainClass.CHOOSE_THE_FORM).click()