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

    # Open the browser with the page.
    webdriver.open_page(page_object.url_candidate)

    # Validate the Login title page.
    webdriver.compare_title(page_object.title_candidates)

    # Parameterize the validation messages.
    fields = [
        (page_object.name_on_table_candidate, "Eddy, Cortez"),
        (page_object.first_name_on_table_candidate, "Aarón"),
        (page_object.last_name_on_table_candidate, "Mena Nuñez"),
        (page_object.city_on_table_candidate, "Puerto La Cruz"),
        (page_object.country_on_table_candidate, "VENEZUELA")]

    # For to verify the text on the required fields.
    for field in fields:
        webdriver.search_clear_input(page_object.search_candidate, field[0], field[1])
