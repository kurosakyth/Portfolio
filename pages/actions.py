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

    # Get element from the page, validate if there is 2 possible selectors, else use only one selector, so is possible to check one selectors if the page is not responsive as expected.
    # Get element from the page, use only one selector
    def get_element(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(selector), BaseException)

        # Find element, send keys and validate the keys sent.
    def send_keys(self, selector, keys_to_send):
        element = self.get_element(selector)
        element.send_keys(keys_to_send)
        actual_keys = element.get_attribute("value")
        assert keys_to_send == actual_keys

    # Method to click / select a button / option on the page.
    def click_btn(self, selector):
        element = self.get_element(selector)
        element.click()

    # Hover the object and click on it.
    def hover_and_click_btn(self, selector):
        element = self.get_element(selector)
        ActionChains(self.driver).move_to_element(element).click().perform()