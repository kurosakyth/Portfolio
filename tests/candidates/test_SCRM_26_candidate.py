import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time

def test_SCRM_26_candidate(browser):
    
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with valid credentials.
    common.login(webdriver, account.username_valid, account.password_valid, page_object.title_homepage)

#CANDIDATE

    # Go to the Candidates page.
    common.all_option_candidate(webdriver)

    # Validate the objects of the Candidate page.
    webdriver.verify_elements_exist([page_object.create_candidate, page_object.view_candidate, page_object.import_candidate,
                                     page_object.recently_viewed_candidate, page_object.h1_title_candidate, page_object.excel_candidate,
                                     page_object.search_candidate, page_object.security_groups_candidate,
                                     page_object.assign_button_candidate, page_object.remove_button_candidate,
                                     page_object.name_column_candidate, page_object.first_name_column_candidate,
                                     page_object.last_name_column_candidate, page_object.city_column_candidate,
                                     page_object.country_column_candidate, page_object.entries_dropdown_candidate,
                                     page_object.entrie_1_option_candidate, page_object.entrie_2_option_candidate,
                                     page_object.entrie_3_option_candidate,page_object.entrie_4_option_candidate,
                                     page_object.toogle_column_candidate, page_object.name_toogle_option_candidate,
                                     page_object.last_name_toogle_option_candidate, page_object.country_toogle_option_candidate,
                                     page_object.city_toogle_option_candidate, page_object.group_dropdown_candidate,
                                     page_object.none_group_option_candidate, page_object.hr_group_option_candidate,
                                     page_object.private_group_option_candidate, page_object.qa_security_group_option_candidate,
                                     page_object.qa_test_group_option_candidate])
    