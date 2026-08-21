import pytest
from selenium import webdriver
from data import BASE_ADDRESS_FROM, BASE_ADDRESS_TO
from pages.choose_route_page import ChooseRoutePage
from pages.main_page import MainPage
from pages.taxi_tariff_page import TaxiTariffPage
from urls import BASE_URL


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    main_page.adding_route(BASE_ADDRESS_FROM, BASE_ADDRESS_TO)
    return main_page

@pytest.fixture
def choose_route_block(driver):
    choose_route_block = ChooseRoutePage(driver)
    return choose_route_block

@pytest.fixture
def taxi_tariff_block(driver):
    taxi_tariff_block = TaxiTariffPage(driver)
    return taxi_tariff_block

# @pytest.fixture
# def 

