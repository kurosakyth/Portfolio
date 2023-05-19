from profiles.test_SCRM_161_profile import test_SCRM_161_profile
from profiles.test_SCRM_252_create_profile import test_SCRM_252_create_profile
from profiles.test_SCRM_254_view_profile import test_SCRM_254_view_profile
from profiles.test_SCRM_278_recruitment_profile import test_SCRM_278_recruitment_profile

def profiles_tests(browser):
    test_SCRM_161_profile(browser)
    test_SCRM_252_create_profile(browser)
    test_SCRM_254_view_profile(browser)
    test_SCRM_278_recruitment_profile(browser)