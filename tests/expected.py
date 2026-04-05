"""
expected.py

Centralized expected UI messages and display values used for test assertions.
"""


class LoginExpected:
    ERROR_EMPTY_CREDENTIALS = "Please enter username and password"
    ERROR_SHORT_PASSWORD = "Password must be at least 4 characters"

class TaskExpected:
    DEFAULT_TIME = "Not specified"
    DEFAULT_DESCRIPTION = "No description"