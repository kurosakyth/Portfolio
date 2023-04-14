import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time

def test_SCRM_353_sort_candidate(browser):
    
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with valid credentials.
    common.login(webdriver, account.username_valid, account.password_valid, page_object.title_homepage)

#CANDIDATE

    # Go to the Candidates page.
    common.all_option_selector(webdriver)

    # Parameterize the validation messages.
    fields = [
        (page_object.name_sort_candidate, page_object.name_on_table_candidate, 'Aarón Alonso, Sibaja Méndez'),
        (page_object.name_sort_candidate, page_object.name_on_table_candidate, 'Óscar, Cordero Fernández'),
        (page_object.first_name_sort_candidate, page_object.first_name_on_table_candidate, 'Aarón'),
        (page_object.first_name_sort_candidate, page_object.first_name_on_table_candidate, 'Óscar'),
        (page_object.last_name_sort_candidate, page_object.last_name_on_table_candidate, 'A'),
        (page_object.last_name_sort_candidate, page_object.last_name_on_table_candidate, 'Zúñiga Morera'),
        (page_object.city_sort_candidate, page_object.city_on_table_candidate, 'Agua caliente'),
        (page_object.city_sort_candidate, page_object.city_on_table_candidate, 'Zona Bananera (Orihueca)'),
        (page_object.country_sort_candidate, page_object.country_on_table_candidate, 'AFGHANISTAN'),
        (page_object.country_sort_candidate, page_object.country_on_table_candidate, 'VENEZUELA')
        ]

    # For to verify the text on the required fields.
    for field in fields:
        webdriver.click_verify(field[0], field[1], field[2])