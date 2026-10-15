import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Ввести адреса: {route_from} -> {route_to}")
    def adding_route(self, route_from, route_to):
        self.set_text(MainPageLocators.DST_FROM_INPUT, route_from)
        self.wait_for_element(MainPageLocators.DST_TO_INPUT)
        self.set_text(MainPageLocators.DST_TO_INPUT, route_to)

    @allure.step("Получить количество точек на карте")
    def get_amount_map_points(self):
        self.wait_for_element(MainPageLocators.MAP_POINTS)
        return len(self.find_elements(MainPageLocators.MAP_POINTS))
