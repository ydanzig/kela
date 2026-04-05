from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object representing the Login page.

    This class encapsulates all locators and business actions related to
    the login flow, such as entering credentials, submitting the form,
    and retrieving validation errors.

    The goal is to keep tests clean, readable, and independent from
    low-level UI implementation details.
    """

    # ======================
    # Locators
    # ======================
    TITLE = '[data-testid="login-title"]'
    USERNAME_INPUT = '[data-testid="login-username"]'
    PASSWORD_INPUT = '[data-testid="login-password"]'
    SUBMIT_BUTTON = '[data-testid="login-submit"]'
    ERROR_MESSAGE = '[data-testid="login-error"]'

    # ======================
    # Page State
    # ======================

    def is_loaded(self) -> bool:
        """
        Verify that the login page is loaded.

        :return: True if the login title is visible, otherwise False.
        """
        return self.is_visible(self.TITLE)

    # ======================
    # Business Actions
    # ======================

    def enter_username(self, username: str):
        """
        Enter a username into the username input field.

        :param username: Username value to enter.
        """
        self.fill(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        """
        Enter a password into the password input field.

        :param password: Password value to enter.
        """
        self.fill(self.PASSWORD_INPUT, password)

    def click_submit(self):
        """
        Click the login submit button.
        """
        self.click(self.SUBMIT_BUTTON)

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
        return self.text(self.ERROR_MESSAGE)

    def is_error_displayed(self) -> bool:
        """
        Check whether a login error message is currently displayed.

        :return: True if the error message is visible, otherwise False.
        """
        return self.is_visible(self.ERROR_MESSAGE)