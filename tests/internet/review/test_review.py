from pages.internet.review import ReviewPageRegion, ReviewPageProvider
import allure
from config import host_stage


@allure.suite("Тесты по отзывам")
class Test101Review:

    @allure.title("Отзыв оставлен на странице региона баг")
    def test_random_review(self, driver):
        review = ReviewPageRegion(driver, url=host_stage + "/ekaterinburg/reviews")
        review.open()
        review.scroll_to_feedback_region()
        review.leave_feedback()

    @allure.title("Отзыв оставлен на странице улицы")
    def test_101_rub_street(self, driver):
        review = ReviewPageRegion(driver, url=host_stage + "/moskva/address/%D0%B0%D1%80%D0%B1%D0%B0%D1%82-id1141/%D1%83%D0%BB-%D0%B0%D1%80%D0%B1%D0%B0%D1%82-id266534")
        review.open()
        review.leave_the_feedback_street()
        review.leave_feedback()

    @allure.title("Отзыв оставлен на странице золотого дома")
    def test_101_rub_house(self, driver):
        review = ReviewPageRegion(driver, url=host_stage + "/moskva/address/%D0%B0%D1%80%D0%B1%D0%B0%D1%82-id1141/%D1%83%D0%BB-%D0%B0%D1%80%D0%B1%D0%B0%D1%82-id266534/d-1-id218520")
        review.open()
        review.leave_the_feedback_golden_house()
        review.leave_feedback()

    # @allure.title("Отзыв оставлен на странице провайдера в разделе отзывы")
    # def test_review_provider_feedback(self, driver):
    #     random_url = random.choice(urls_provider_feedback)
    #     review = ReviewPageProvider(driver, random_url)
    #     review.open()
    #     review.scroll_to_feedback_provider_feedback()
    #     review_2 = ReviewPageRegion(driver, random_url)
    #     review_2.leave_feedback()
    #     print("Выбранный URL:", random_url)

    @allure.title("Отзыв оставлен на главной странице")
    def test_review_main_page(self, driver):
        review = ReviewPageRegion(driver, url=host_stage + "/chelyabinsk")
        review.open()
        review.scroll_to_feedback_maim_page()
        review.leave_feedback()

    @allure.title("Отзыв оставлен на странице офиса")
    def test_review_office(self, driver):
        review = ReviewPageRegion(driver, url=host_stage + "/chelyabinsk/orders/office")
        review.open()
        review.scroll_to_feedback_maim_page()
        review.leave_feedback()

    @allure.title("Отзыв оставлен на странице загородной заявки")
    def test_review_dacha(self, driver):
        review = ReviewPageRegion(driver, url=host_stage + "/chelyabinsk/orders/sat")
        review.open()
        review.scroll_to_feedback_maim_page()
        review.leave_feedback()