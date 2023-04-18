import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time

def test_SCRM_27_availability_related(browser):
    
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

    # Search for a Candidate.
    webdriver.send_keys_to_element(page_object.search_candidate, 'Walden')

    # Click on the candidate searched.
    webdriver.click_button(page_object.result_searched_test_candidate)

    # Verify the candidate title of the page.
    webdriver.compare_title(page_object.title_walden_candidate_view)

#SELECT A AVAILABILITY RELATED

    # Display the subpanel.
    webdriver.click_button(page_object.availab_related_view_candidate)

    # Click on the Select to open the new window.
    webdriver.click_button(page_object.select_availab_related_view_candidate)

    # Get a list of all the open windows
    window_handles = browser.window_handles

    # Switch to the latest window (the new window)
    window = window_handles[-1]
    browser.switch_to.window(window)

    webdriver.click_button(page_object.option_select_availab_related_view_candidate)

#CREATE A AVAILABILITY RELATED
    # Switch back to the original window.
    window = window_handles[0]
    browser.switch_to.window(window)

    # Click on the create button.
    webdriver.click_button(page_object.create_availab_related_view_candidate)
    
    # Click on the hour start time dropdown.
    webdriver.dropdown_select(page_object.hour_start_time_create_related_view_candidate, "11")

    # Click on the hour start time dropdown.
    webdriver.dropdown_select(page_object.minutes_start_time_create_related_view_candidate, "15")

    # Click on the hour start time dropdown.
    webdriver.dropdown_select(page_object.hour_end_time_create_related_view_candidate, "12")

    # Click on the hour start time dropdown.
    webdriver.dropdown_select(page_object.minutes_end_time_create_related_view_candidate, "15")

    # Click on the save button to create the request on the subpanel.
    webdriver.click_button(page_object.save_button_availab_related_view_candidate)
    time.sleep(5)