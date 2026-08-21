import allure
from selenium.webdriver.support.ui import WebDriverWait
from locators.taxi_search_locators import TaxiSearchLocators
from pages.base_page import BasePage


class TaxiSearchPage(BasePage):

    @allure.step("Проверить отображение окна ожидания")
    def is_waiting_form_displayed(self):
        return self.wait_for_element(TaxiSearchLocators.ORDER_CONTAINER).is_displayed()

    @allure.step("Получить заголовок окна ожидания")
    def get_waiting_title(self):
        return self.find_element(TaxiSearchLocators.WAITING_TITLE).text

    @allure.step("Проверить отображение таймера")
    def is_timer_displayed(self):
        return self.find_element(TaxiSearchLocators.TIMER).is_displayed()

    @allure.step("Дождаться завершения заказа")
    def wait_for_order_complete(self, timeout=35):
        WebDriverWait(self.driver, timeout).until(
            lambda _: 'приедет' in self.find_element(TaxiSearchLocators.WAITING_TITLE).text
        )

    @allure.step("Получить заголовок заказа")
    def get_order_title(self):
        return self.find_element(TaxiSearchLocators.WAITING_TITLE).text

    @allure.step("Проверить отображение номера машины")
    def is_car_number_displayed(self):
        return self.find_element(TaxiSearchLocators.CAR_NUMBER).is_displayed()

    @allure.step("Проверить отображение изображения машины")
    def is_car_image_displayed(self):
        return self.wait_for_element_clickable(TaxiSearchLocators.CAR_IMAGE).is_displayed()

    @allure.step("Получить имя водителя")
    def get_driver_name(self):
        return self.find_element(TaxiSearchLocators.DRIVER_NAME).text

    @allure.step("Получить рейтинг водителя")
    def get_driver_rating(self):
        return self.wait_for_element_clickable(TaxiSearchLocators.DRIVER_RATING).text

    @allure.step("Проверить отображение фото водителя")
    def is_driver_photo_displayed(self):
        return self.wait_for_element_clickable(TaxiSearchLocators.DRIVER_PHOTO).is_displayed()

    @allure.step("Нажать кнопку Детали")
    def click_details_button(self):
        self.wait_for_element_clickable(TaxiSearchLocators.DETAILS_BUTTON).click()

    @allure.step("Нажать кнопку Отмена")
    def click_cancel_button(self):
        self.wait_for_element_clickable(TaxiSearchLocators.CANCEL_BUTTON).click()

    @allure.step("Получить стоимость поездки")
    def get_trip_price(self):
        return self.wait_for_element(TaxiSearchLocators.TRIP_PRICE).text

    @allure.step("Проверить что окно заказа закрылось")
    def is_order_closed(self):
        containers = self.find_elements(TaxiSearchLocators.ORDER_CONTAINER)
        if not containers:
            return True
        return not containers[0].is_displayed()
