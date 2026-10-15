import allure
from locators.choose_route_locators import ChooseRouteLocators
from pages.base_page import BasePage


class ChooseRoutePage(BasePage):

    @allure.step("Проверить отображение блока выбора маршрута")
    def is_choose_route_block_displayed(self):
        element = self.find_element(ChooseRouteLocators.CHOOSE_ROUTE_BLOCK)
        return 'shown' in element.get_attribute('class')

    @allure.step("Получить текст стоимости маршрута")
    def get_results_info_text(self):
        return self.wait_for_element_clickable(ChooseRouteLocators.INFO_TEXT)

    @allure.step("Получить время в пути")
    def get_results_info_duration(self):
        return self.wait_for_element_clickable(ChooseRouteLocators.INFO_DURATION)

    @allure.step("Переключить на режим Оптимальный")
    def switch_optimal_mode(self):
        self.find_element(ChooseRouteLocators.OPTIMAL_MODE).click()

    @allure.step("Переключить на режим Быстрый")
    def switch_fast_mode(self):
        self.find_element(ChooseRouteLocators.FAST_MODE).click()

    @allure.step("Переключить на режим Свой")
    def switch_custom_mode(self):
        self.find_element(ChooseRouteLocators.CUSTOM_MODE).click()

    @allure.step("Выбрать тип передвижения Драйв")
    def switch_to_drive(self):
        self.find_element(ChooseRouteLocators.DRIVE_TYPE).click()

    @allure.step("Получить активный режим маршрута")
    def get_active_mode(self):
        return self.wait_for_element(ChooseRouteLocators.ACTIVE_MODE)

    @allure.step("Проверить что типы передвижения неактивны")
    def is_types_disabled(self):
        types_block = self.find_elements(ChooseRouteLocators.TYPES_BLOCK)
        for type_block in types_block:
            if 'disabled' in type_block.get_attribute('class'):
                return True
        return False

    @allure.step("Проверить отображение кнопки Вызвать такси")
    def is_taxi_button_displayed(self):
        taxi_button = self.wait_for_element(ChooseRouteLocators.TAXI_BUTTON)
        return taxi_button.is_displayed()

    @allure.step("Проверить отображение кнопки Забронировать")
    def is_drive_button_displayed(self):
        drive_button = self.find_element(ChooseRouteLocators.DRIVE_BUTTON)
        return drive_button.is_displayed()

    @allure.step("Нажать кнопку Вызвать такси")
    def click_taxi_button(self):
        taxi_button = self.wait_for_element_clickable(ChooseRouteLocators.TAXI_BUTTON)
        taxi_button.click()
