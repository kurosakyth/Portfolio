import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time

def test_SCRM_322_edit_candidate(browser):
    
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with valid credentials.
    common.login(webdriver, account.username_valid, account.password_valid, page_object.title_homepage)

    #CANDIDATE

    # Go to the Candidates page.
    common.all_option_selector(webdriver)

    # Search for a Candidate.
    webdriver.send_keys_to_element(page_object.search_candidate, 'Walden')

    # Click on the candidate searched.
    webdriver.click_button(page_object.result_searched_test_candidate)

    # Verify the view candidate title of the page == to walden.
    webdriver.compare_title(page_object.title_walden_candidate_view)

    # Click on edit button.
    webdriver.click_button(page_object.edit_view_candidate)

    # Verify the edit candidate title of the page == to walden.
    webdriver.compare_title(page_object.title_edit_walden)

    # Validate the objects of the Candidate page.
    webdriver.verify_elements_exist([page_object.first_name_candidate_edit, page_object.last_name_candidate_edit,
                                     page_object.document_candidate_edit, page_object.email_candidate_edit,
                                     page_object.mobile_candidate_edit, page_object.country_candidate_edit,
                                     page_object.city_candidate_edit, page_object.state_province_candidate_edit,
                                     page_object.employed_candidate_edit, page_object.employer_candidate_edit,
                                     page_object.years_of_experience_candidate_edit, page_object.save_btn_create_candidate,
                                     page_object.cancel_btn_candidate_edit, page_object.upload_btn_candidate_edit,
                                     page_object.educa_candidate_diploma_edit, page_object.educa_candidate_adgd_edit,
                                     page_object.educa_candidate_babs_edit, page_object.educa_candidate_mamsmba_edit,
                                     page_object.educa_candidate_md_edit, page_object.educa_candidate_jd_edit,
                                     page_object.educa_candidate_phd_edit, page_object.educa_candidate_doc_edit])

    # Parameterize information to write on the form.
    fields_to_fill_the_information = [
    (page_object.first_name_candidate_edit, 'Waldina'),
    (page_object.last_name_candidate_edit, 'Schmidtita'),
    (page_object.document_candidate_edit, '11111111'),
    (page_object.email_candidate_edit, 'walschmidt@gmail.kom'),
    (page_object.mobile_candidate_edit, '11111111'),
    (page_object.country_candidate_edit, 'Rusia'),
    (page_object.city_candidate_edit, 'Moscow'),
    (page_object.state_province_candidate_edit, 'Zelenograd')]
    
    
    # Overwrite the input with the new information.
    for field in fields_to_fill_the_information:
        webdriver.overwrite_input_sending_keys(field[0], field[1])

    # Click on the Save button.
    webdriver.click_button(page_object.save_btn_create_candidate)

    # Validate the waldina title page.
    webdriver.compare_title(page_object.title_view_waldina)