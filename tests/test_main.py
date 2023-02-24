from test_login import test_login
from test_logout import test_logout
from test_invoices import test_invoices
from test_create_invoices import test_create_invoices

def all_tests(browser):
    test_invoices(browser)
    test_login(browser)
    test_logout(browser)
    test_create_invoices(browser)
    