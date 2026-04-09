"""
Login page tests.

Test Coverage:
- Total test functions: 3
- Total executed test cases: 10

| Test Name                    | Test Type               | Description                                                               |
|------------------------------|-------------------------|---------------------------------------------------------------------------|
| test_login_success           | Positive, Sanity, Parametrized | Verify successful login with multiple valid credential combinations|      |
| test_login_validation_errors | Negative, Parametrized  | Verify validation errors for multiple invalid login attempts              |
| test_logout_success          | State, Sanity           | Verify that a logged-in user can log out successfully                     |
"""

import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from tests.expected import LoginExpected


############################################################################################
######################################## Positive Tests ####################################
############################################################################################

@pytest.mark.sanity
@pytest.mark.login
@pytest.mark.positive
@pytest.mark.parametrize(
    "username, password",
    [
        ("yoni", "1234"),
        ("Yoni", "abcd"),
        ("user_01", "pass1234"),
    ],
    ids=[
        "valid_basic_credentials",
        "valid_mixed_case_username",
        "valid_username_with_underscore",
    ],
)
def test_login_success(page, username, password):
    """
    Verify that a user can log in successfully with valid credentials.
    """
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.login(username, password)

    assert dashboard_page.is_loaded(), \
        "Dashboard page was not loaded after successful login."

    assert username in dashboard_page.get_logged_in_user(), \
        f"Logged-in username is not displayed as expected. Expected to display '{username}' in the user element, but got '{dashboard_page.get_logged_in_user()}'."

############################################################################################
######################################## Negative Tests ####################################
############################################################################################

@pytest.mark.login
@pytest.mark.negative
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("", "", LoginExpected.ERROR_EMPTY_CREDENTIALS),
        ("Moshe", "123", LoginExpected.ERROR_SHORT_PASSWORD),
        ("", "1234", LoginExpected.ERROR_EMPTY_CREDENTIALS),
        ("Yoni", "", LoginExpected.ERROR_EMPTY_CREDENTIALS),
        ("   ", "1234", LoginExpected.ERROR_EMPTY_CREDENTIALS),
        ("David", "   ", LoginExpected.ERROR_EMPTY_CREDENTIALS),
    ],
    ids=[
        "empty_username_and_password",
        "password_shorter_than_minimum",
        "empty_username_only",
        "empty_password_only",
        "username_contains_only_spaces",
        "password_contains_only_spaces",
    ],
)
def test_login_validation_errors(page, username, password, expected_error):
    """
    Verify that invalid login attempts display the expected validation error message.
    """
    login_page = LoginPage(page)

    login_page.login(username, password)

    assert login_page.is_error_displayed(), \
        f"Expected validation error message was not displayed. Expected: '{expected_error}' but got '{login_page.get_error_message()}'."

    assert login_page.get_error_message() == expected_error, \
        f"Unexpected error message. Expected: '{expected_error}'. but got: '{login_page.get_error_message()}'."
    
############################################################################################
######################################## State Tests #######################################
############################################################################################

@pytest.mark.sanity
@pytest.mark.login
@pytest.mark.state
def test_logout_success(page):
    """
    Verify that a logged-in user can log out successfully and is redirected to login page.
    """
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # Perform login
    login_page.login("yoni", "1234")

    assert dashboard_page.is_loaded(), \
        "Dashboard page was not loaded after login."

    # Perform logout
    dashboard_page.logout()

    # Verify login page is shown again
    assert login_page.is_loaded(), \
        "Login page was not displayed after logout."