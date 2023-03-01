from test_login_SCRM_2 import test_login_SCRM_2
from test_logout_SCRM_1 import test_logout_SCRM_1
from test_invoices_SCRM_43 import test_invoices_SCRM_43
from test_login_invalid_SCRM_347 import test_login_SCRM_347
# from test_create_invoices import test_create_invoices
# from test_invoices_search import test_invoices_search

def all_tests(browser):
    test_login_SCRM_2(browser)
    test_logout_SCRM_1(browser)
    test_invoices_SCRM_43(browser)
    test_login_SCRM_347(browser)
    # test_create_invoices(browser)
    # test_invoices_search(browser)