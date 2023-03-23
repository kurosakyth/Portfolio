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

    # Write on the input using the name on the table.
    webdriver.search_clear_input(page_object.search_candidate, page_object.name_on_table_candidate, "Eddy, Cortez")

    # Write on the input using the first name with accent mark on the table. 
    webdriver.search_clear_input(page_object.search_candidate, page_object.first_name_on_table_candidate, "Aarón")
 
    # Write on the input using the last name with 'ñ' on the table.
    webdriver.search_clear_input(page_object.search_candidate, page_object.last_name_on_table_candidate, "Mena Nuñez")

    # Write on the input using the city with spaces on the table. 
    webdriver.search_clear_input(page_object.search_candidate, page_object.city_on_table_candidate, "Puerto La Cruz")

    # Write on the input using the country with capital letters on the table. 
    webdriver.search_clear_input(page_object.search_candidate, page_object.country_on_table_candidate, "VENEZUELA")