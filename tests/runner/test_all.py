from login.test_SCRM_2_login import test_SCRM_2_login
from login.test_SCRM_1_logout import test_SCRM_1_logout
from login.test_SCRM_347_login_invalid import test_SCRM_347_login_invalid 
# from test_invoices_SCRM_43 import test_invoices_SCRM_43
# from test_create_invoices import test_create_invoices
# from test_invoices_search import test_invoices_search

def all_tests(browser):
    test_SCRM_2_login(browser)
    test_SCRM_1_logout(browser)
    test_SCRM_347_login_invalid(browser)
    # test_invoices_SCRM_43(browser)
    # test_create_invoices(browser)
    # test_invoices_search(browser)