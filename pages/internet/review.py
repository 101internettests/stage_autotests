import allure
import time
from locators.internet.review import ReviewOnTheHouse, ReviewMainPage, ReviewOperator, ReviewProvider
from locators.internet.review import ReviewForRegion, ReviewOnTheStreet, ReviewProviderFeedback
from pages.base_page import BasePage
from selenium.webdriver import ActionChains


class ReviewPageRegion(BasePage):

    @allure.step("Скролл  до кнопки оставления отзыва и клик на нее")
    def scroll_to_feedback_region(self):
        time.sleep(3)
        scroll = self.element_is_visible(ReviewForRegion.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(ReviewForRegion.LEAVE_FEEDBACK).click()
        time.sleep(3)

    @allure.step("Оставление отзыва")
    def leave_feedback(self):
        self.element_is_visible(ReviewForRegion.CHOOSE_PROVIDER).click()
        self.element_is_visible(ReviewForRegion.CLICK_PROVIDER).click()
        self.element_is_visible(ReviewForRegion.CHOOSE_INTERNET).click()
        self.element_is_visible(ReviewForRegion.CLICK_INTERNET).click()
        self.element_is_visible(ReviewForRegion.CHOOSE_TIME).click()
        self.element_is_visible(ReviewForRegion.CHOOSE_SERVISE).click()
        self.element_is_visible(ReviewForRegion.CLICK_RATING).click()
        self.element_is_visible(ReviewForRegion.ENTER_FEEDBACK).send_keys(
            "ТЕСТ. Это тестовый отзыв оставленный роботом для проверки отделом тестирования. Он будет проверен и деактивирован.")
        self.element_is_visible(ReviewForRegion.LEAVE_FEEDBACK_2).click()
        self.element_is_visible(ReviewForRegion.CLICK_ANONIM).click()
        time.sleep(3)
        close = self.element_is_present(ReviewForRegion.SUCCESS_POPAP)
        assert close.text == "Спасибо за отзыв!"

    @allure.step("Скролл  до кнопки оставления отзыва на главной и клик на нее")
    def scroll_to_feedback_maim_page(self):
        time.sleep(3)
        scroll = self.element_is_visible(ReviewMainPage.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(ReviewMainPage.LEAVE_FEEDBACK).click()
        time.sleep(3)

    @allure.step("Оставление отзыва на улице")
    def leave_the_feedback_street(self):
        time.sleep(3)
        scroll = self.element_is_visible(ReviewOnTheStreet.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(ReviewOnTheStreet.ClICK_FEEDBACK).click()
        time.sleep(3)

    @allure.step("Оставление отзыва на золотом доме")
    def leave_the_feedback_golden_house(self):
        time.sleep(3)
        scroll = self.element_is_visible(ReviewOnTheStreet.SCROLL_GOLDEN_HOUSE)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(ReviewOnTheStreet.ClICK_FEEDBACK).click()
        time.sleep(3)

    @allure.step("Оставление отзыва у оператора")
    def leave_the_feedback_101_pub_operator(self):
        time.sleep(3)
        scroll = self.element_is_visible(ReviewOperator.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(ReviewOperator.LEAVE_FEEDBACK).send_keys(
            "ТЕСТ. Со страницы оператора. Это тестовый отзыв оставленный роботом для проверки отделом тестирования. Он будет проверен и деактивирован.")
        self.element_is_visible(ReviewOnTheStreet.LEAVE_NAME).send_keys("Тест")
        time.sleep(3)
        self.element_is_visible(ReviewOperator.CHOOCE_OPERATOR).click()
        time.sleep(3)
        self.element_is_visible(ReviewOperator.CLICK_OPERATOR).click()
        time.sleep(3)
        self.element_is_visible(ReviewOperator.LEAVE_FEEDBACK_2).click()
        time.sleep(3)
        close = self.element_is_present(ReviewOperator.CLOSE_THE_POPAP)
        assert close.text == "Спасибо за отзыв!"


class ReviewPageProvider(BasePage):
    @allure.step("Скролл до кнопки оставления отзыва в карточке провайдера и клик на нее")
    def scroll_to_feedback_provider(self):
        time.sleep(3)
        scroll = self.element_is_visible(ReviewProvider.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(ReviewForRegion.LEAVE_FEEDBACK).click()
        time.sleep(3)

    @allure.step("Оставление отзыва у провайдера")
    def leave_feedback_provider(self):
        self.element_is_visible(ReviewForRegion.CHOOSE_INTERNET).click()
        self.element_is_visible(ReviewForRegion.CLICK_INTERNET).click()
        self.element_is_visible(ReviewForRegion.CHOOSE_TIME).click()
        self.element_is_visible(ReviewForRegion.CHOOSE_SERVISE).click()
        self.element_is_visible(ReviewForRegion.CLICK_RATING).click()
        self.element_is_visible(ReviewForRegion.ENTER_FEEDBACK).send_keys(
            "ТЕСТ. Это тестовый отзыв оставленный роботом для проверки отделом тестирования. Он будет проверен и деактивирован.")
        self.element_is_visible(ReviewForRegion.LEAVE_FEEDBACK_2).click()
        self.element_is_visible(ReviewForRegion.CLICK_ANONIM).click()
        time.sleep(3)
        close = self.element_is_present(ReviewForRegion.SUCCESS_POPAP)
        assert close.text == "Спасибо за отзыв!"

    @allure.step("Скролл до кнопки оставления отзыва в карточке провайдера в разделе отзывы и клик на нее")
    def scroll_to_feedback_provider_feedback(self):
        time.sleep(3)
        scroll = self.element_is_visible(ReviewForRegion.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(ReviewProviderFeedback.LEAVE_FEEDBACK).click()
        time.sleep(3)
