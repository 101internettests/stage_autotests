import allure
from pages.internet.search import CheckPage404, CheckTheCoverageMap
import time
from config import host_stage


@allure.suite("Тесты поиск на 101")
class TestSearch:
    @allure.title("Проверка отображения страницы 404 при запросе несуществующего URL")
    def test_check_page_404(self, driver):
         search_page = CheckPage404(driver, url=host_stage + "/moskva/rating/onlime/741")
         search_page.open()
         search_page.find_text_404()

    @allure.title("Автоматический поиск не дал результатов при поиске с несуществующим адресом")
    def test_nonexistent_address_101(self, driver):
        search_page = CheckPage404(driver, url=host_stage + "/chelyabinsk")
        search_page.open()
        search_page.check_nonexistent_address()

    @allure.title("Проверка карты покрытия в Челябинске падает")
    def test_map_chb(self, driver):
        search_page = CheckTheCoverageMap(driver, url=host_stage + "/")
        search_page.open()
        search_page.change_region_on_chb()
        search_page.check_search_gold_house()
        search_page.check_the_buttons()
        time.sleep(3)
        search_page.pangination_batymsksya()
        search_page.change_region_on_chb()