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

    # Open the browser with the page.
    webdriver.open_page(page_object.url_candidate)

    # Validate the Login title page.
    webdriver.compare_title(page_object.title_candidates)

    fields = [
            (page_object.name_sort_candidate, 'sorting_asc'),
            (page_object.name_sort_candidate, 'sorting_desc'),
            (page_object.first_name_sort_candidate, 'sorting_asc'),
            (page_object.first_name_sort_candidate, 'sorting_desc'),
            (page_object.last_name_sort_candidate, 'sorting_asc'),
            (page_object.last_name_sort_candidate, 'sorting_desc'),
            (page_object.city_sort_candidate, 'sorting_asc'),
            (page_object.city_sort_candidate, 'sorting_desc'),
            (page_object.country_sort_candidate, 'sorting_asc'),
            (page_object.country_sort_candidate, 'sorting_desc')
            ]

    # For to verify the text on the required fields.
    for field in fields:
        webdriver.click_asc_desc(field[0], field[1])