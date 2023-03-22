import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time

def test_SCRM_331_search_candidate(browser):
    
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with valid credentials.
    common.login(webdriver, account.username_valid, account.password_valid, page_object.title_homepage)

    #CANDIDATE

    # Go to the Candidates page.
    common.all_option_selector(webdriver)

    # Search a specific word on the search input.
    webdriver.send_keys_to_element(page_object.search_candidate, "Eddy, Cortez")

    # Validate the search made on the table.
    webdriver.verify_text(page_object.name_on_table_candidate, "Eddy, Cortez")

    # time.sleep(5)