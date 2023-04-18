from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class actions:

    # Constructor.
    def __init__(self, driver):
        self.driver = driver

    # Open the page with the link.
    def open_page(self ,url):
        self.driver.get(url) 

    # Validate the title of the page and compare if it is correct. 
    def compare_title(self, title_expected):
        WebDriverWait(self.driver, 10).until(ec.title_is(title_expected))
        assert self.driver.title == title_expected

    # Get element from the page.
    def get_element(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(selector), BaseException)
    
    # Method to click / select a button / option on the page.
    def click_button(self, selector):
        self.get_element(selector).click()

    # Method to select an option from a dropdown by value.
    def dropdown_select(self, selector, option):
        dropdown = Select(self.get_element(selector))
        dropdown.select_by_value(option)
    
    # Find element, send keys and validate the keys sent.
    def send_keys_to_element(self, selector, keys_to_send):
        element = self.get_element(selector)
        element.send_keys(keys_to_send)
        actual_keys = element.get_attribute("value")
        assert keys_to_send == actual_keys

    # Clear an input to send keys after that.
    def overwrite_input_sending_keys(self, selector, keys_to_send):
        self.clear_input(selector)
        self.send_keys_to_element(selector, keys_to_send)

    # Hover the object and click on it.
    def hover_and_click_element(self, selector):
        element = self.get_element(selector)
        ActionChains(self.driver).move_to_element(element).click().perform()

    # Method to validate the text from the page.
    def verify_text(self, selector, expected_text):
        element = self.get_element(selector)
        actual_text = element.text
        assert actual_text == expected_text

    # Method to clear an input.
    def clear_input(self, selector):
        element = self.get_element(selector)
        element.clear()

    # Write on the search input and clear it after verify the information searched.
    def search_clear_input(self, search_element, element_on_table, text):
        self.send_keys_to_element(search_element, text)
        self.verify_text(element_on_table, text)
        self.clear_input(search_element)

    def click_asc_desc(self, element, class_expected):
        self.click_button(element)
        self.check_asc_desc(element, class_expected)

    # Verify the class of the element.
    def check_asc_desc(self, selector, class_expected):
        element = self.get_element(selector)
        class_name = element.get_attribute("class")
        assert class_expected in class_name

    # Method get the elements from the page to create the list.
    def get_elements_from_page(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_all_elements_located(selector), BaseException)

    # Method to validate that the elements on the page are displayed.
    def verify_elements_exist(self, locators):
        elements = []
        for locator in locators:
            elements += self.get_elements_from_page(locator)

        # Assert that the elements were displayed.
        for element in elements:
            assert element.is_displayed()

    def alert_click(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    