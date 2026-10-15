from selenium.webdriver.common.by import By

class MainPageLocators:
    MAP_BLOCK = (By.ID, "map")
    MAP_POINTS = (By.XPATH, ".//ymaps[contains(@class, 'routerPoints')]//ymaps[contains(@class, 'pin__b')]")

    DST_BLOCK = (By.XPATH, "//div[@class='dst-picker']")
    DST_FROM_INPUT = (By.ID, "from")
    DST_TO_INPUT = (By.ID, "to")

