import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time

def test_SCRM_352_sort_candidate(browser):
    
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with valid credentials.
    common.login(webdriver, account.username_valid, account.password_valid, page_object.title_homepage)

#CANDIDATE

    # Go to the Candidates page.
    common.all_option_selector(webdriver)

    # Ascending name.
    webdriver.click_verify(page_object.name_sort_candidate, page_object.name_on_table_candidate, 'Aarón Alonso, Sibaja Méndez')

    # Descending name.
    webdriver.click_verify(page_object.name_sort_candidate, page_object.name_on_table_candidate, 'Óscar, Cordero Fernández')

    # Ascending first name.
    webdriver.click_verify(page_object.first_name_sort_candidate, page_object.first_name_on_table_candidate, 'Aarón')

    # Descending first name.
    webdriver.click_verify(page_object.first_name_sort_candidate, page_object.first_name_on_table_candidate, 'Óscar')

    # Ascending last name.
    webdriver.click_verify(page_object.last_name_sort_candidate, page_object.last_name_on_table_candidate, 'A')

    # Descending last name.
    webdriver.click_verify(page_object.last_name_sort_candidate, page_object.last_name_on_table_candidate, 'Zúñiga Morera')

    # Ascending city.
    webdriver.click_verify(page_object.city_sort_candidate, page_object.city_on_table_candidate, 'Agua caliente')

    # Descending city.
    webdriver.click_verify(page_object.city_sort_candidate, page_object.city_on_table_candidate, 'Zona Bananera (Orihueca)')

    # Ascending country.
    webdriver.click_verify(page_object.country_sort_candidate, page_object.country_on_table_candidate, 'AFGHANISTAN')

    # Descending country.
    webdriver.click_verify(page_object.country_sort_candidate, page_object.country_on_table_candidate, 'VENEZUELA')

    # time.sleep(5)