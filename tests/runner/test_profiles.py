from profiles.test_SCRM_161_profile import test_SCRM_161_profile
from profiles.test_SCRM_252_create_profile import test_SCRM_252_create_profile

def profiles_tests(browser):
    test_SCRM_161_profile(browser)
    test_SCRM_252_create_profile(browser)