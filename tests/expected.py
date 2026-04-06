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

class UrgentEventExpected:
    TYPE_REQUIRED = "Event type is required" #Not in use yet. cannot identify the element for this error message, but added for future use when the element will be added to the page.
    PLEASE_SELECT_ITEM = "Please select an item in the list."
    ATTACK_EVENT_TEXT = "Attack event"
    ASSAULT_EVENT_TEXT = "Assault event"
    BREACH_EVENT_TEXT = "Breach event"
    RED_EVENT_TEXT = "Red event"