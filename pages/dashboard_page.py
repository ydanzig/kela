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
    URGENT_EVENT_TYPE = '[data-testid="urgent-event-type"]'
    URGENT_EVENT_TIME = '[data-testid="urgent-event-time"]'
    URGENT_EVENT_DESCRIPTION = '[data-testid="urgent-event-description"]'

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

    def open_add_urgent_event(self):
        """
        Open the Add Urgent Event modal.
        """
        self.click(self.ADD_URGENT_BTN)

    def select_urgent_event_type(self, event_type: str):
        """
        Select urgent event type from dropdown.
        """
        self.page.locator(self.URGENT_TYPE_SELECT).select_option(event_type)

    def fill_urgent_event_time(self, time: str):
        """
        Fill urgent event time field.
        """
        self.fill(self.URGENT_TIME_INPUT, time)

    def fill_urgent_event_description(self, description: str):
        """
        Fill urgent event description field.
        """
        self.fill(self.URGENT_DESCRIPTION_INPUT, description)

    def set_urgent_toggle(self, value: bool):
        """
        Set urgent checkbox to the requested state.
        """
        checkbox = self.page.locator(self.URGENT_TOGGLE)
        if checkbox.is_checked() != value:
            checkbox.click()

    def click_add_urgent_event(self):
        """
        Click Add button in urgent event modal.
        """
        self.click(self.URGENT_ADD_BTN)

    def add_urgent_event(
        self,
        event_type: str = "",
        time: str = "",
        description: str = "",
        urgent: bool = False,
    ):
        """
        Add a new urgent event.

        Allows flexible usage for both positive and negative scenarios.
        """
        self.open_add_urgent_event()

        if event_type:
            self.select_urgent_event_type(event_type)

        if time:
            self.fill_urgent_event_time(time)

        if description:
            self.fill_urgent_event_description(description)

        self.set_urgent_toggle(urgent)
        self.click_add_urgent_event()

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

    def first_urgent_event_text(self) -> str:
        """
        Return full text of the first urgent event card.
        """
        return self.page.locator(self.URGENT_ITEMS).first.inner_text()
    
    def is_urgent_type_select_invalid(self) -> bool:
        """
        Check if the urgent event type select element is in an invalid state (e.g. after trying to submit without selecting a type).
        """
        return self.page.locator(self.URGENT_TYPE_SELECT).evaluate(
            "el => !el.checkValidity()"
    )

    def urgent_type_validation_message(self) -> str:
        """
        Get the validation message of the urgent event type select element.
        """
        return self.page.locator(self.URGENT_TYPE_SELECT).evaluate(
            "el => el.validationMessage"
        )

    def first_urgent_event_type(self) -> str:
        """
        Return the type of the first displayed urgent event.
        """
        return self.page.locator(self.URGENT_EVENT_TYPE).first.inner_text()

    def first_urgent_event_time(self) -> str:
        """
        Return the time of the first displayed urgent event.
        """
        return self.page.locator(self.URGENT_EVENT_TIME).first.inner_text()

    def first_urgent_event_description(self) -> str:
        """
        Return the description of the first displayed urgent event.
        """
        return self.page.locator(self.URGENT_EVENT_DESCRIPTION).first.inner_text()
    
    def first_urgent_event_is_marked_red(self) -> bool:
        """
        Check if first urgent event has red styling.
        """
        classes = self.page.locator(self.URGENT_ITEMS).first.get_attribute("class")
        return "urgent-event-red" in classes
    # ======================
    # Business Actions - Events History
    # ======================

    def ensure_events_history_open(self):
        """
        Ensure that the events history section is open.
        If it is already visible, do nothing. Otherwise, open it.
        """
        if not self.is_visible(self.EVENTS_SECTION):
            self.click(self.VIEW_EVENTS_BTN)

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
    
    def first_event_row_text(self) -> str:
        """
        Return full text of the first event row.
        """
        return self.page.locator(self.EVENT_ROWS).first.inner_text()
    
    def all_event_rows_text(self) -> list[str]:
        """
        Return text of all event rows.
        """
        return self.page.locator(self.EVENT_ROWS).all_inner_texts()

    # ======================
    # User Actions
    # ======================

    def logout(self):
        """
        Logout from the application.
        """
        self.click(self.LOGOUT)