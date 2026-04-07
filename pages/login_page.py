from pages.maps.login_map import LoginMap
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object representing the Login page.

    This class encapsulates business actions related to
    the login flow, such as entering credentials, submitting the form,
    and retrieving validation errors.

    The goal is to keep tests clean, readable, and independent from
    low-level UI implementation details.
    """
    def __init__(self, page):
        super().__init__(page)
        self.map = LoginMap

    # ======================
    # Page State
    # ======================

    def is_loaded(self) -> bool:
        """
        Verify that the login page is loaded.

        :return: True if the login title is visible, otherwise False.
        """
        return self.is_visible(self.map.TITLE)

    # ======================
    # Business Actions
    # ======================

    def enter_username(self, username: str):
        """
        Enter a username into the username input field.

        :param username: Username value to enter.
        """
        self.fill(self.map.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        """
        Enter a password into the password input field.

        :param password: Password value to enter.
        """
        self.fill(self.map.PASSWORD_INPUT, password)

    def click_submit(self):
        """
        Click the login submit button.
        """
        self.click(self.map.SUBMIT_BUTTON)

    def login(self, username: str, password: str):
        """
        Perform a complete login action.

        :param username: Username to use for login.
        :param password: Password to use for login.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()

    # ======================
    # Getters / Validations
    # ======================

    def get_error_message(self) -> str:
        """
        Get the displayed login error message.

        :return: Error message text.
        """
        return self.text(self.map.ERROR_MESSAGE)

    def is_error_displayed(self) -> bool:
        """
        Check whether a login error message is currently displayed.

        :return: True if the error message is visible, otherwise False.
        """
        return self.is_visible(self.map.ERROR_MESSAGE)