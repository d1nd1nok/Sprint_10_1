import allure
import pytest
from pages.main_page import MainPage
from data import BASE_ADDRESS_FROM, BASE_ADDRESS_TO


class TestMain:

    @allure.title("На карте отображаются две точки при вводе разных адресов")
    # @pytest.mark.parametrize("route_from, route_to",
    #                          [(BASE_ADDRESS_FROM, BASE_ADDRESS_TO),
    #                           (BASE_ADDRESS_TO, BASE_ADDRESS_FROM)])
    def test_route_rendering(self, driver, main_page):
        assert main_page.get_amount_map_points() == 2
