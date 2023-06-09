#LOGIN
from login.test_SCRM_2_login import test_SCRM_2_login
from login.test_SCRM_1_logout import test_SCRM_1_logout
from login.test_SCRM_347_login_invalid import test_SCRM_347_login_invalid 
#CANDIDATES
from candidates.test_SCRM_82_create_candidate import test_SCRM_82_create_candidate
from candidates.test_SCRM_26_candidate import test_SCRM_26_candidate
from candidates.test_SCRM_331_search_candidate import test_SCRM_331_search_candidate
from candidates.test_SCRM_353_sort_candidate import test_SCRM_353_sort_candidate
from candidates.test_SCRM_81_delete_candidate import test_SCRM_81_delete_candidate
from candidates.test_SCRM_324_view_candidate import test_SCRM_324_view_candidate
from candidates.test_SCRM_322_edit_candidate import test_SCRM_322_edit_candidate
from candidates.test_SCRM_120_select_candidate import test_SCRM_120_select_candidate
from candidates.test_SCRM_28_select_job_offer import test_SCRM_28_select_job_offer
from candidates.test_SCRM_354_select_note import test_SCRM_354_select_note
from candidates.test_SCRM_352_select_interview import test_SCRM_352_select_interview
from candidates.test_SCRM_27_availability_related import test_SCRM_27_availability_related
from candidates.test_SCRM_360_track_log_relates import test_SCRM_360_track_log_relates
from candidates.test_SCRM_360_track_log_relates import test_SCRM_360_track_log_relates
from candidates.test_SCRM_294_special_notes import test_SCRM_294_special_notes
from candidates.test_SCRM_356_personality import test_SCRM_356_personality
from candidates.test_SCRM_255_qualifications import test_SCRM_255_qualifications
from candidates.test_SCRM_359_duplicate_candidate import test_SCRM_359_duplicate_candidate
#Profiles
from profiles.test_SCRM_161_profile import test_SCRM_161_profile
from profiles.test_SCRM_252_create_profile import test_SCRM_252_create_profile

#INVOICES
# from test_invoices_SCRM_43 import test_invoices_SCRM_43
# from test_create_invoices import test_create_invoices
# from test_invoices_search import test_invoices_search

def all_tests(browser):
    #Login
    test_SCRM_2_login(browser)
    test_SCRM_1_logout(browser)
    test_SCRM_347_login_invalid(browser)

    #Candidates
    test_SCRM_82_create_candidate(browser)
    test_SCRM_26_candidate(browser)
    test_SCRM_331_search_candidate(browser)
    test_SCRM_353_sort_candidate(browser)
    test_SCRM_324_view_candidate(browser)
    test_SCRM_322_edit_candidate(browser)
    test_SCRM_120_select_candidate(browser)
    test_SCRM_28_select_job_offer(browser)
    test_SCRM_354_select_note(browser)
    test_SCRM_352_select_interview(browser)
    test_SCRM_27_availability_related(browser)
    test_SCRM_360_track_log_relates(browser)
    test_SCRM_294_special_notes(browser)
    test_SCRM_356_personality(browser)
    test_SCRM_255_qualifications(browser)
    test_SCRM_359_duplicate_candidate(browser)
    test_SCRM_81_delete_candidate(browser)#This should run after the create candidate have finished, so should be at the end of the list.

    #Profiles
    test_SCRM_161_profile(browser)
    test_SCRM_252_create_profile(browser)

    # test_invoices_SCRM_43(browser)
    # test_create_invoices(browser)
    # test_invoices_search(browser)