from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time
class actions:

    # Constructor.
    def __init__(self, driver):
        self.driver = driver

    # Open the page with the link.
    def load_page(self ,selector):
        self.driver.get(selector) 

    # Validate the title of the page and compare if it is correct. 
    def title_compare(self, title_expected):
        assert self.driver.title == title_expected

    # Get element from the page.
    def get_element(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(selector), BaseException)
    
    # Get element to be clickable.
    def get_element_to_click(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(selector), BaseException)

    # Find element, send keys and validate the keys sent.
    def send_keys(self, selector, keys_to_send):
        element = self.get_element(selector)
        element.send_keys(keys_to_send)
        actual_keys = element.get_attribute("value")
        assert keys_to_send == actual_keys

    # Method to click / select a button / option on the page.
    # def click_btn(self, selector):
    #     element = self.get_element_to_click(selector)
    #     element.click()

    def click_btn(self, selector):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((selector))).click()

    # Hover the object and click on it.
    def hover_and_click_btn(self, selector):
        element = self.get_element(selector)
        ActionChains(self.driver).move_to_element(element).click().perform()

