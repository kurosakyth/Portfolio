import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time
from selenium.webdriver.common.alert import Alert

def test_SCRM_331_search_candidate(browser):
    
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with valid credentials.
    common.login(webdriver, account.username_valid, account.password_valid, page_object.title_homepage)

    #CANDIDATE

    # Go to the Candidates page.
    common.all_option_selector(webdriver)

    # Write on the search input for a candidate.
    webdriver.send_keys_to_element(page_object.search_candidate, 'Walden')

    # Click on the candidate searched.
    webdriver.click_button(page_object.result_searched_test_candidate)

    # Verify the candidate title of the page.
    webdriver.compare_title(page_object.title_walden_candidate_view)
    
    # Click on delete button on the candidate view.
    webdriver.click_button(page_object.delete_view_candidate)

    # Accept the alert to delete.
    webdriver.alert_click()

    # Verify the candidate title of the page.
    webdriver.compare_title(page_object.title_candidates)