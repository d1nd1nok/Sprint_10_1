import allure
from data import TARIFF_DESCRIPTIONS
from locators.taxi_tariff_locators import TaxiTariffLocators
from pages.base_page import BasePage


class TaxiTariffPage(BasePage):

    @allure.step("Проверить отображение блока тарифов")
    def is_tariff_block_displayed(self):
        tariff_block = self.wait_for_element(TaxiTariffLocators.TARIFF_BLOCK)
        return tariff_block.is_displayed()

    @allure.step("Получить количество карточек тарифов")
    def get_tariff_cards_count(self):
        return len(self.find_elements(TaxiTariffLocators.ALL_TARIFF_CARDS))

    @allure.step("Проверить отображение полей формы заказа")
    def is_form_with_fields_displayed(self):
        form = self.find_element(TaxiTariffLocators.TARIFF_FORM)
        phone = self.find_element(TaxiTariffLocators.PHONE_INPUT)
        payment = self.find_element(TaxiTariffLocators.PAYMENT_TYPE)
        comm = self.find_element(TaxiTariffLocators.COMMENT_INPUT)
        reqs = self.find_element(TaxiTariffLocators.REQS_INPUT)
        return all([form, phone, payment, comm, reqs])

    @allure.step("Проверить описание каждого тарифа")
    def check_tariff_description(self):
        expected = TARIFF_DESCRIPTIONS
        self.wait_for_element(TaxiTariffLocators.TARIFF_BLOCK)
        cards = self.find_elements(TaxiTariffLocators.ALL_TARIFF_CARDS)

        for card in cards:
            if 'active' not in card.get_attribute('class'):
                card.click()
            info_button = self.wait_for_element(TaxiTariffLocators.TARIFF_INFO_BUTTON)
            self.navigate(info_button)
            desc_element = self.wait_for_element(TaxiTariffLocators.TARIFF_DESCRIPTION)
            name = self.wait_for_element_clickable(TaxiTariffLocators.ACTIVE_TARIFF_NAME).text
            desc_text = desc_element.text
            if expected[name] != desc_text:
                return False
            self.navigate(self.wait_for_element_clickable(TaxiTariffLocators.TARIFF_BLOCK))
        return True

    @allure.step("Получить цену активного тарифа")
    def get_active_tariff_price(self):
        return self.find_element(TaxiTariffLocators.ACTIVE_TARIFF_PRICE).text

    @allure.step("Открыть блок Требования к заказу")
    def open_requirements(self):
        self.click_element(TaxiTariffLocators.REQS_HEADER)

    @allure.step("Включить чекбокс Столик для ноутбука")
    def enable_laptop_table(self):
        self.click_element(TaxiTariffLocators.LAPTOP_SWITCH)

    @allure.step("Нажать кнопку Ввести номер и заказать")
    def click_order_button(self):
        self.click_element(TaxiTariffLocators.ORDER_BUTTON)
