from candidates.test_SCRM_82_create_candidate import test_SCRM_82_create_candidate
from candidates.test_SCRM_26_candidate import test_SCRM_26_candidate
from candidates.test_SCRM_331_search_candidate import test_SCRM_331_search_candidate
from candidates.test_SCRM_352_sort_candidate import test_SCRM_352_sort_candidate
from candidates.test_SCRM_81_delete_candidate import test_SCRM_81_delete_candidate
from candidates.test_SCRM_324_view_candidate import test_SCRM_324_view_candidate

def candidates_tests(browser):
    test_SCRM_82_create_candidate(browser)
    test_SCRM_26_candidate(browser)
    test_SCRM_331_search_candidate(browser)
    test_SCRM_352_sort_candidate(browser)
    test_SCRM_324_view_candidate(browser)
    test_SCRM_81_delete_candidate(browser)#This should run after the create candidate have finished, so should be at the end of the list.