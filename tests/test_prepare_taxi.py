import allure
from pages.choose_route_page import ChooseRoutePage
from pages.main_page import MainPage
from data import BASE_ADDRESS_FROM, BASE_ADDRESS_TO


class TestPrepareTaxi:

    @allure.title("Переключение режима меняет время и стоимость маршрута")
    def test_switching_mode_changes_time_and_cost(self, driver, main_page, choose_route_block):
        choose_route_block.switch_optimal_mode()
        optimal_time = choose_route_block.get_results_info_duration().text
        optimal_cost = choose_route_block.get_results_info_text().text
        choose_route_block.switch_fast_mode()
        fast_time = choose_route_block.get_results_info_duration().text
        fast_cost = choose_route_block.get_results_info_text().text
        active_mode = choose_route_block.get_active_mode().text
        assert optimal_time != fast_time or optimal_cost != fast_cost
        assert active_mode == "Быстрый"

    @allure.title("В режиме Свой активны типы передвижения")
    def test_custom_mode_changes_active_mode(self, driver, main_page, choose_route_block):
        choose_route_block.switch_custom_mode()
        assert not choose_route_block.is_types_disabled()

    @allure.title("В режиме Быстрый доступна кнопка Вызвать такси")
    def test_fast_mode_available_taxi_button(self, driver, main_page, choose_route_block):
        choose_route_block.switch_fast_mode()
        assert choose_route_block.is_taxi_button_displayed()

    @allure.title("В режиме Свой с типом Драйв доступна кнопка Забронировать")
    def test_custom_mode_available_drive_button(self, driver, main_page, choose_route_block):
        choose_route_block.switch_custom_mode()
        choose_route_block.switch_to_drive()
        assert choose_route_block.is_drive_button_displayed()
