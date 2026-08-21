from selenium.webdriver.common.by import By

class TaxiSearchLocators:
    # Окно заказа (общий контейнер)
    ORDER_CONTAINER = (By.XPATH, "//div[@class='order shown']")

    # Окно ожидания
    WAITING_TITLE = (By.XPATH, "//div[@class='order-header-title']")
    TIMER = (By.XPATH, "//div[@class='order-header-time']")

    # Кнопки Отменить / Детали
    CANCEL_BUTTON = (By.XPATH, "//button[@class='order-button']/img[@alt='close']")
    DETAILS_BUTTON = (By.XPATH, "//button[@class='order-button']/img[@alt='burger']")

    # Окно совершённого заказа
    CAR_NUMBER = (By.XPATH, "//div[@class='number']")
    CAR_IMAGE = (By.XPATH, "//div[@class='order-number']/img[@alt='Car']")
    DRIVER_NAME = (By.XPATH, "//div[@class='order-btn-group'][1]//div[not(@class)]")
    DRIVER_RATING = (By.XPATH, "//div[@class='order-btn-rating']")
    DRIVER_PHOTO = (By.XPATH, "//div[@class='order-btn-group'][1]//div[@class='order-button']/img")

    # Блок деталей (раскрывается по кнопке Детали)
    DETAILS_BLOCK = (By.XPATH, "//div[@class='order-details shown']")
    TRIP_PRICE = (By.XPATH, "//div[@class='o-d-h'][text()='Еще про поездку']/following-sibling::div[@class='o-d-sh']")
