import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time

def test_SCRM_254_view_profile(browser):
    
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with valid credentials.
    common.login(webdriver, account.username_valid, account.password_valid, page_object.title_homepage)

#PROFILE

    # Open the browser with the page.
    webdriver.open_page(page_object.url_profile)
   
    # Validate the Login title page.
    webdriver.compare_title(page_object.title_profile)

    # Click on the first profile on the list.
    webdriver.click_button(page_object.option_on_the_table_profile)


    # Verify the candidate title of the page.
    webdriver.compare_title(page_object.title_contains_view_profile)

    # Display all the subpanels.
    webdriver.click_button(page_object.skills_quallifications_sub_view_profile)
    webdriver.click_button(page_object.profile_match_sub_view_profile)
    webdriver.click_button(page_object.recruitment_request_sub_view_profile)
    webdriver.click_button(page_object.job_description_sub_profile)
    webdriver.click_button(page_object.job_offer_view_profile)
    webdriver.click_button(page_object.security_groups_view_profile)

    # Validate the objects of the Candidate page.
    webdriver.verify_elements_exist([page_object.edit_button_view_profile, page_object.duplicate_button_view_profile,
                                     page_object.delete_button_view_profile, page_object.find_button_duplicate_view_profile,
                                     page_object.view_change_log_button_view_profile, page_object.previous_arrow_view_profile,
                                     page_object.next_arrow_view_profile, # Buttons

                                     page_object.basic_sub_view_profile, page_object.name_basic_view_profile,
                                     page_object.system_only_basic_view_profile, # Basic sub

                                     page_object.skills_quallifications_sub_view_profile, page_object.h3_sk_view_profile,
                                     page_object.show_entries_sk_view_profile, page_object.select_a_sk_view_profile,
                                     page_object.name_sk_view_profile, page_object.expected_rating_sk_view_profile,
                                     page_object.experience_sk_view_profile, page_object.showing_entries_sk_view_profile,
                                     page_object.previous_sk_view_profile, page_object.next_sk_view_profile, # Skills

                                     page_object.h3_quali_view_profile, page_object.show_entries_quali_view_profile,
                                     page_object.favourites_quali_view_profile, page_object.select_quali_view_profile,
                                     page_object.name_quali_view_profile, page_object.level_quali_view_profile,
                                     page_object.suport_requiered_quali_view_profile, page_object.showing_entries_quali_view_profile,
                                     page_object.previous_quali_view_profile, page_object.next_quali_view_profile, # Qualifications

                                     page_object.profile_match_sub_view_profile, page_object.employees_prof_match_view_profile,
                                     page_object.candidates_prof_match_view_profile, page_object.active_only_prof_match_view_profile,
                                     page_object.unassigned_only_prof_match_view_profile, page_object.copy_btn_prof_match_view_profile,
                                     page_object.pdf_btn_prof_match_view_profile, page_object.csv_btn_prof_match_view_profile,
                                     page_object.excel_btn_prof_match_view_profile, page_object.show_rows_btn_prof_match_view_profile,
                                     page_object.name_column_prof_match_view_profile, page_object.country_law_column_prof_match_view_profile,
                                     page_object.english_column_prof_match_view_profile, page_object.profile_rating_column_prof_match_view_profile,
                                     page_object.active_column_prof_match_view_profile, page_object.is_assigned_column_prof_match_view_profile,
                                     page_object.chart_column_prof_match_view_profile, # Profile Matches
                                    
                                     page_object.all_sub_view_profile, page_object.careers_sub_view_profile,
                                     page_object.hr_sub_view_profile, page_object.other_sub_view_profile, # Options

                                     page_object.recruitment_request_sub_view_profile, page_object.job_description_sub_profile,
                                      page_object.job_offer_view_profile, page_object.security_groups_view_profile]) # Recuitment Request