import pages.locators as page_object
from pages.functions import actions
from pages.common import login
import credentials.credentials as account
import time

def test_SCRM_331_search_candidate(browser):
    
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with valid credentials.
    login(webdriver, account.username_valid, account.password_valid, page_object.title_homepage)

    # Mouse hover and click all.
    webdriver.hover_and_click_element(page_object.all_dropdown)

    # Click the candidates option on All.
    webdriver.click_button(page_object.candidate_option)

#CANDIDATES

    # Validate the Candidates title page.
    webdriver.compare_title(page_object.title_candidates)

    # Search a specific word on the search input.
    webdriver.send_keys_to_element(page_object.search_candidate, "Eddy, Cortez")

    # Validar la búsqueda.
    webdriver.verify_text(page_object.name_on_table_candidate, "Eddy, Cortez")

    # time.sleep(5)