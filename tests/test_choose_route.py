import allure
from pages.choose_route_page import ChooseRoutePage
from pages.main_page import MainPage
from data import BASE_ADDRESS_FROM, BASE_ADDRESS_TO


class TestChooseRoute:

    @allure.title("Блок выбора маршрута отображается при вводе разных адресов")
    def test_choose_route_block_displayed(self, driver, main_page, choose_route_block):
        assert choose_route_block.is_choose_route_block_displayed()

    @allure.title("При одинаковых адресах отображается Авто Бесплатно и 0 мин")
    def test_choose_route_with_same_addresses(self, driver, choose_route_block):
        main_page = MainPage(driver)
        main_page.adding_route(BASE_ADDRESS_FROM, BASE_ADDRESS_FROM)
        assert choose_route_block.get_results_info_text().text == "Авто Бесплатно"
        assert choose_route_block.get_results_info_duration().text == "В пути 0 мин."
