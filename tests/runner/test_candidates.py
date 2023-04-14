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

def candidates_tests(browser):
    test_SCRM_82_create_candidate(browser)
    test_SCRM_26_candidate(browser)
    test_SCRM_331_search_candidate(browser)
    test_SCRM_353_sort_candidate(browser)
    test_SCRM_324_view_candidate(browser)
    test_SCRM_322_edit_candidate(browser)
    test_SCRM_120_select_candidate(browser)
    test_SCRM_28_select_job_offer(browser)
    test_SCRM_354_select_note(browser)
    test_SCRM_81_delete_candidate(browser)#This should run after the create candidate have finished, so should be at the end of the list.