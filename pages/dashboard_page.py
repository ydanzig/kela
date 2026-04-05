from pages.base_page import BasePage


class DashboardPage(BasePage):
    """
    Page Object representing the Dashboard screen .

    This page includes:
    - Task management (add/delete tasks)
    - Urgent event handling
    - Events history view

    Provides high-level business actions used in test scenarios.
    """

    # ======================
    # Locators
    # ======================
    TITLE = '[data-testid="dashboard-title"]'
    USER = '[data-testid="user-display"]'
    LOGOUT = '[data-testid="logout-btn"]'

    # Tasks
    ADD_TASK_BTN = '[data-testid="add-task-btn"]'
    TASK_NAME_INPUT = '[data-testid="task-name-input"]'
    TASK_TIME_INPUT = '[data-testid="task-time-input"]'
    TASK_DESCRIPTION_INPUT = '[data-testid="task-description-input"]'
    TASK_ADD_BTN = '[data-testid="task-add-btn"]'
    TASK_ITEMS = '[data-testid="task-item"]'
    TASK_NAMES = '[data-testid="task-name"]'
    DELETE_TASK_BTNS = '[data-testid="delete-task-btn"]'
    NO_TASKS_MESSAGE = '[data-testid="no-tasks-message"]'
    TASK_TIMES = '[data-testid="task-time"]'
    TASK_DESCRIPTIONS = '[data-testid="task-description"]'

    # Urgent Events
    ADD_URGENT_BTN = '[data-testid="add-urgent-event-btn"]'
    URGENT_TYPE_SELECT = '[data-testid="urgent-event-type-select"]'
    URGENT_TIME_INPUT = '[data-testid="urgent-event-time-input"]'
    URGENT_DESCRIPTION_INPUT = '[data-testid="urgent-event-description-input"]'
    URGENT_TOGGLE = '[data-testid="urgent-event-toggle"]'
    URGENT_ADD_BTN = '[data-testid="urgent-event-add-btn"]'
    URGENT_ITEMS = '[data-testid="urgent-event-item"]'
    DELETE_URGENT_BTNS = '[data-testid="delete-urgent-event-btn"]'

    # Events History
    VIEW_EVENTS_BTN = '[data-testid="view-events-btn"]'
    EVENTS_SECTION = '[data-testid="events-section"]'
    EVENT_ROWS = '[data-testid="event-row"]'
    NO_EVENTS_MESSAGE = '[data-testid="no-events-message"]'

    # ======================
    # Page State
    # ======================

    def is_loaded(self) -> bool:
        """
        Verify that the dashboard page is loaded.
        """
        return self.is_visible(self.TITLE)

    # ======================
    # Business Actions - Tasks
    # ======================

    def add_task(self, name: str, time: str = "", description: str = ""):
        """
        Add a new task.

        :param name: Task name (required)
        :param time: Optional time
        :param description: Optional description
        """
        self.click(self.ADD_TASK_BTN)
        self.fill(self.TASK_NAME_INPUT, name)
        self.fill(self.TASK_TIME_INPUT, time)
        self.fill(self.TASK_DESCRIPTION_INPUT, description)
        self.click(self.TASK_ADD_BTN)

    def delete_first_task(self):
        """
        Delete the first task displayed in the task list.
        """
        self.page.locator(self.DELETE_TASK_BTNS).first.click()

    def task_count(self) -> int:
        """
        Get number of tasks.
        """
        return self.page.locator(self.TASK_ITEMS).count()

    def first_task_name(self) -> str:
        """
        Return the name of the first displayed task.
        """
        return self.page.locator(self.TASK_NAMES).first.inner_text()
    
    def first_task_time(self) -> str:
        """
        Return the time of the first displayed task.
        """
        return self.page.locator(self.TASK_TIMES).first.inner_text()

    def first_task_description(self) -> str:
        """
        Return the description of the first displayed task.
        """
        return self.page.locator(self.TASK_DESCRIPTIONS).first.inner_text()
    # ======================
    # Business Actions - Urgent Events
    # ======================

    def add_urgent_event(
        self,
        event_type: str,
        time: str = "",
        description: str = "",
        urgent: bool = False,
    ):
        """
        Add a new urgent event.

        :param event_type: Type of event (must match dropdown option)
        :param time: Optional time
        :param description: Optional description
        :param urgent: Whether to toggle urgency flag
        """
        self.click(self.ADD_URGENT_BTN)
        self.page.locator(self.URGENT_TYPE_SELECT).select_option(event_type)

        if time:
            self.fill(self.URGENT_TIME_INPUT, time)

        if description:
            self.fill(self.URGENT_DESCRIPTION_INPUT, description)

        if urgent:
            self.click(self.URGENT_TOGGLE)

        self.click(self.URGENT_ADD_BTN)

    def delete_first_urgent_event(self):
        """
        Delete the first urgent event.
        """
        self.page.locator(self.DELETE_URGENT_BTNS).first.click()

    def urgent_event_count(self) -> int:
        """
        Get number of urgent events.
        """
        return self.page.locator(self.URGENT_ITEMS).count()

    # ======================
    # Business Actions - Events History
    # ======================

    def open_events_history(self):
        """
        Open events history section.
        """
        self.click(self.VIEW_EVENTS_BTN)

    def event_count(self) -> int:
        """
        Get number of events in history.
        """
        return self.page.locator(self.EVENT_ROWS).count()

    # ======================
    # User Actions
    # ======================

    def logout(self):
        """
        Logout from the application.
        """
        self.click(self.LOGOUT)