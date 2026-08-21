import allure
from pages.choose_route_page import ChooseRoutePage
from pages.main_page import MainPage
from pages.taxi_tariff_page import TaxiTariffPage
from pages.taxi_search_page import TaxiSearchPage
from data import BASE_ADDRESS_FROM, BASE_ADDRESS_TO


class TestSearchTaxi:

    @allure.title("Появляется окно ожидания машины с заголовком и таймером")
    def test_waiting_screen(self, driver, main_page, choose_route_block, taxi_tariff_block):
        choose_route_block.switch_fast_mode()
        choose_route_block.click_taxi_button()
        taxi_tariff_block.is_tariff_block_displayed()
        taxi_tariff_block.open_requirements()
        taxi_tariff_block.enable_laptop_table()
        taxi_tariff_block.click_order_button()
        search_page = TaxiSearchPage(driver)
        assert search_page.is_waiting_form_displayed()
        assert search_page.is_timer_displayed()

    @allure.title("После таймера отображается окно совершённого заказа")
    def test_order_complete(self, driver, main_page, choose_route_block, taxi_tariff_block):
       
        choose_route_block.switch_fast_mode()
        choose_route_block.click_taxi_button()
        taxi_tariff_block.is_tariff_block_displayed()
        taxi_tariff_block.open_requirements()
        taxi_tariff_block.enable_laptop_table()
        taxi_tariff_block.click_order_button()
        search_page = TaxiSearchPage(driver)
        search_page.wait_for_order_complete()
        assert search_page.is_car_number_displayed()
        assert search_page.is_car_image_displayed()
        assert search_page.get_driver_name()
        assert search_page.get_driver_rating()
        assert search_page.is_driver_photo_displayed()

    @allure.title("В деталях указана стоимость тарифа, кнопка Отмена закрывает окно")
    def test_details_price_and_cancel(self, driver, main_page, choose_route_block, taxi_tariff_block):
       
        choose_route_block.switch_fast_mode()
        choose_route_block.click_taxi_button()
        taxi_tariff_block.is_tariff_block_displayed()
        tariff_price = taxi_tariff_block.get_active_tariff_price()
        taxi_tariff_block.open_requirements()
        taxi_tariff_block.enable_laptop_table()
        taxi_tariff_block.click_order_button()
        search_page = TaxiSearchPage(driver)
        search_page.wait_for_order_complete()
        search_page.click_details_button()
        trip_price = search_page.get_trip_price()
        assert tariff_price.replace(" ", "") in trip_price.replace(" ", "")
        search_page.click_cancel_button()
        assert search_page.is_order_closed()
