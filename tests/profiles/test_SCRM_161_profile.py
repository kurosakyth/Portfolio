import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time

def test_SCRM_161_profiles(browser):
    
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with valid credentials.
    common.login(webdriver, account.username_valid, account.password_valid, page_object.title_homepage)

#PROFILES

    # Go to the Candidates page.
    common.all_option_profile(webdriver)

    webdriver.verify_elements_exist([page_object.create_profile,page_object.view_profile,
                                    page_object.import_profile, page_object.recently_viewed_profile,
                                    page_object.recently_viewed_profile, page_object.system_only_column_profile,
                                    page_object.name_column_profile, page_object.published_column_profile,
                                    page_object.bulk_button_profile, page_object.filter_button_profile,
                                    page_object.column_chooser_button_profile, page_object.start_arrow_profile,
                                    page_object.previous_arrow_profile, page_object.next_arrow_profile,
                                    page_object.end_arrow_profile, page_object.assign_button_candidate,
                                    page_object.remove_button_candidate, page_object.group_dropdown_candidate,
                                     page_object.none_group_option_candidate, page_object.hr_group_option_candidate,
                                     page_object.private_group_option_candidate, page_object.qa_security_group_option_candidate,
                                     page_object.qa_test_group_option_candidate])

    webdriver.click_button(page_object.checkbox_dropdown_profile)

    webdriver.verify_elements_exist([page_object.select_this_page_checkbox_option_profile,
                                    page_object.select_all_checkbox_option_profile,
                                    page_object.deselect_checkbox_option_profile])