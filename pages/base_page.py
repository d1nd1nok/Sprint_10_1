from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def click_element(self, locator):
        self.find_element(locator).click()

    def set_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def get_current_url(self):
        return self.driver.current_url
    
    def open(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    
    def navigate(self, element):
        ActionChains(self.driver).move_to_element(element).perform()
    