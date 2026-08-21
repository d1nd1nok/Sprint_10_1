from selenium.webdriver.common.by import By

class ChooseRouteLocators:
    CHOOSE_ROUTE_BLOCK = (By.XPATH, "//div[contains(@class, 'type-picker')]")

    MODES_BLOCK = (By.XPATH, "//div[@class='modes-container']")
    OPTIMAL_MODE = (By.XPATH, "//div[contains(text(), 'Оптимальный')]")
    FAST_MODE = (By.XPATH, "//div[contains(text(), 'Быстрый')]")
    CUSTOM_MODE = (By.XPATH, "//div[contains(text(), 'Свой')]")
    ACTIVE_MODE = (By.XPATH, "//div[@class='modes-container']/div[contains(@class, 'active')]")


    TYPES_BLOCK = (By.XPATH, "//div[@class='types-container']")
    CAR_TYPE = (By.XPATH, "//div[@class='types-container']//img[contains(@src, 'car')]")                                        
    WALK_TYPE = (By.XPATH, "//div[@class='types-container']//img[contains(@src, 'walk')]")                                      
    TAXI_TYPE = (By.XPATH, "//div[@class='types-container']//img[contains(@src, 'taxi')]")                                    
    BICYCLE_TYPE = (By.XPATH, "//div[@class='types-container']//img[contains(@src, 'bike')]")
    SCOOTER_TYPE = (By.XPATH, "//div[@class='types-container']//img[contains(@src, 'scooter')]")
    DRIVE_TYPE = (By.XPATH, "//div[@class='types-container']//img[contains(@src, 'drive')]")
    ACTIVE_TYPE = (By.XPATH, "//div[@class='types-container']/div[contains(@class, 'active')]")

    INFO_BLOCK = (By.XPATH, "//div[@class='results-text']")
    INFO_TEXT = (By.XPATH, ".//div[@class='text']")
    INFO_DURATION = (By.XPATH, ".//div[@class='duration']")

    DRIVE_BUTTON = (By.XPATH, ".//button[@type='button' and contains(text(), 'Забронировать')]")
    TAXI_BUTTON = (By.XPATH, ".//button[@type='button' and contains(text(), 'Вызвать такси')]")





