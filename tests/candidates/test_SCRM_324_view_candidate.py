import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time

def test_SCRM_324_view_candidate(browser):
    
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

    # Validate the objects of the Candidate page.
    webdriver.verify_elements_exist([page_object.edit_button_view_candidate, page_object.duplicate_button_view_candidate,
                                     page_object.delete_button_view_candidate, page_object.find_button_duplicate_view_candidate,
                                     page_object.view_change_log_button_view_candidate, page_object.basic_subp_view_candidate,
                                     page_object.name_view_candidate, page_object.exp_educ_sub_view_candidate,
                                     page_object.profile_match_sub_view_candidate, page_object.all_match_sub_view_candidate,
                                     page_object.activities_match_sub_view_candidate, page_object.invoices_match_sub_view_candidate,
                                     page_object.recruitment_match_sub_view_candidate, page_object.other_match_sub_view_candidate,
                                     page_object.candidate_accounts_view_candidate, page_object.job_offer_view_candidate,
                                     page_object.candidate_note_view_candidate, page_object.interviews_view_candidate,
                                     page_object.availab_related_view_candidate, page_object.track_log_related_view_candidate,
                                     page_object.skills_view_candidate, page_object.special_notes_view_candidate,
                                     page_object.personality_test_view_candidate, page_object.qualifications_view_candidate,
                                     page_object.security_groups_view_candidate])