from pages.internet.tags import OneHundredMainPage
from pages.main_page import MainPage
import allure
from config import host_stage


@allure.suite("Тесты теговые на 101")
class TestOneHundredInternetTags:
    @allure.title("Воронеж - тарифы, теги: 'интернет и моб. связь', 'интернет и тв и моб. связь', 'домашний интернет' падает")
    def test_voronezh_tags(self, driver):
        tags = OneHundredMainPage(driver, url=host_stage + "/voronezh")
        tags.open()
        tags.open_rates()
        tags.send_application_region_tag()

    @allure.title("Екатеринбург - ростелеком, теги: 'интернет и моб. связь' падает")
    def test_ekb_rostelecom_tags(self, driver):
        tags = OneHundredMainPage(driver, url=host_stage + "/ekaterinburg/providers/rostelecom/rates/internet-i-mobilnaya-svyaz")
        tags.open()
        tags.new_application_provider_ekb()