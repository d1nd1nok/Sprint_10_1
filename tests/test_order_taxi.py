import allure
from pages.choose_route_page import ChooseRoutePage
from pages.main_page import MainPage
from pages.taxi_tariff_page import TaxiTariffPage
from data import BASE_ADDRESS_FROM, BASE_ADDRESS_TO


class TestOrderTaxi:

    @allure.title("Открывается форма заказа с 6 тарифами")
    def test_tariff_block_opened(self, driver, main_page, choose_route_block, taxi_tariff_block):
        choose_route_block.click_taxi_button()
        assert taxi_tariff_block.is_tariff_block_displayed()
        assert taxi_tariff_block.get_tariff_cards_count() == 6

    @allure.title("Под тарифами отображаются поля Телефон, Оплата, Комментарий, Требования")
    def test_tariff_block_fields_displayed(self, driver, main_page, choose_route_block, taxi_tariff_block):
        choose_route_block.click_taxi_button()
        assert taxi_tariff_block.is_form_with_fields_displayed()

    @allure.title("Описание каждого тарифа соответствует ТЗ")
    def test_tariff_description(self, driver, main_page, choose_route_block, taxi_tariff_block):
        choose_route_block.click_taxi_button()
        assert taxi_tariff_block.check_tariff_description()
