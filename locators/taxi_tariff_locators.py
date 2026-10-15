from selenium.webdriver.common.by import By


class TaxiTariffLocators:
    TARIFF_BLOCK = (By.XPATH, "//div[@class='tariff-cards']")

    ALL_TARIFF_CARDS = (By.XPATH, "//div[@class='tcard' or @class='tcard active']")
    ACTIVE_TARIFF_CARD = (By.XPATH, "//div[@class='tcard active']")
    ACTIVE_TARIFF_NAME = (By.XPATH, "//div[@class='tcard active']//div[@class='tcard-title']")
    ACTIVE_TARIFF_PRICE = (By.XPATH, "//div[@class='tcard active']//div[@class='tcard-price']")
    TARIFF_INFO_BUTTON = (By.XPATH, "//div[@class='tcard active']//button[contains(@class,'i-button')]")
    TARIFF_DESCRIPTION = (By.XPATH, "//div[@class='tcard active']//div[@class='i-dPrefix']")

    TARIFF_FORM = (By.XPATH, "//div[@class='form']")
    PHONE_INPUT = (By.XPATH, "//div[@class='np-button']")
    PAYMENT_TYPE = (By.XPATH, "//div[contains(@class, 'pp-text') and contains(text(), 'Способ оплаты')]")
    COMMENT_INPUT = (By.ID, "comment")
    REQS_INPUT = (By.XPATH, "//div[@class = 'reqs']")

    REQS_HEADER = (By.XPATH, "//div[@class='reqs-header']")
    LAPTOP_SWITCH = (By.XPATH, "//div[@class='r-sw-label'][text()='Столик для ноутбука']/following-sibling::div//span[@class='slider round']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='smart-button']")
