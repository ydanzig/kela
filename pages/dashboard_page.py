import allure
from pages.maps.dashboard_map import DashboardMap
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

    def __init__(self, page):
        super().__init__(page)
        self.map = DashboardMap

    # ======================
    # Page State
    # ======================

    def is_loaded(self) -> bool:
        """
        Verify that the dashboard page is loaded.
        """
        return self.is_visible(self.map.TITLE)

    # ======================
    # Tasks - Actions
    # ======================

    @allure.step("Add task: {name}")
    def add_task(self, name: str, time: str = "", description: str = ""):
        """
        Add a new task.

        :param name: Task name (required)
        :param time: Optional time
        :param description: Optional description
        """
        self.click(self.map.ADD_TASK_BTN)
        self.fill(self.map.TASK_NAME_INPUT, name)
        self.fill(self.map.TASK_TIME_INPUT, time)
        self.fill(self.map.TASK_DESCRIPTION_INPUT, description)
        self.click(self.map.TASK_ADD_BTN)

    @allure.step("Delete first task")
    def delete_first_task(self):
        """
        Delete the first task displayed in the task list.
        """
        self.locator(self.map.DELETE_TASK_BTNS).first.click()

    # ==============================
    # Tasks - Getters / Validations
    # ==============================

    def task_count(self) -> int:
        """
        Get number of tasks.
        """
        return self.count(self.map.TASK_ITEMS)

    def first_task_name(self) -> str:
        """
        Return the name of the first displayed task.
        """
        return self.first_text(self.map.TASK_NAMES)
    
    def first_task_time(self) -> str:
        """
        Return the time of the first displayed task.
        """
        return self.first_text(self.map.TASK_TIMES)

    def first_task_description(self) -> str:
        """
        Return the description of the first displayed task.
        """
        return self.first_text(self.map.TASK_DESCRIPTIONS)
    
    # ========================
    # Urgent Events - Actions
    # ========================

    def open_add_urgent_event(self):
        """
        Open the Add Urgent Event modal.
        """
        self.click(self.map.ADD_URGENT_BTN)

    def select_urgent_event_type(self, event_type: str):
        """
        Select urgent event type from dropdown.
        """
        self.locator(self.map.URGENT_TYPE_SELECT).select_option(event_type)

    def fill_urgent_event_time(self, time: str):
        """
        Fill urgent event time field.
        """
        self.fill(self.map.URGENT_TIME_INPUT, time)

    def fill_urgent_event_description(self, description: str):
        """
        Fill urgent event description field.
        """
        self.fill(self.map.URGENT_DESCRIPTION_INPUT, description)

    def set_urgent_toggle(self, value: bool):
        """
        Set urgent checkbox to the requested state.
        """
        checkbox = self.locator(self.map.URGENT_TOGGLE)
        if checkbox.is_checked() != value:
            checkbox.click()

    def click_add_urgent_event(self):
        """
        Click Add button in urgent event modal.
        """
        self.click(self.map.URGENT_ADD_BTN)

    @allure.step("Add urgent event: {event_type}")
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

    @allure.step("Delete first urgent event")
    def delete_first_urgent_event(self):
        """
        Delete the first urgent event.
        """
        self.locator(self.map.DELETE_URGENT_BTNS).first.click()
    
    # =====================================
    # Urgent Events - Getters / Validations
    # =====================================

    def urgent_event_count(self) -> int:
        """
        Get number of urgent events.
        """
        return self.count(self.map.URGENT_ITEMS)

    def first_urgent_event_text(self) -> str:
        """
        Return full text of the first urgent event card.
        """
        return self.first_text(self.map.URGENT_ITEMS)
    
    def is_urgent_type_select_invalid(self) -> bool:
        """
        Check if the urgent event type select element is in an invalid state (e.g. after trying to submit without selecting a type).
        """
        return self.locator(self.map.URGENT_TYPE_SELECT).evaluate(
            "el => !el.checkValidity()"
    )

    def urgent_type_validation_message(self) -> str:
        """
        Get the validation message of the urgent event type select element.
        """
        return self.locator(self.map.URGENT_TYPE_SELECT).evaluate(
            "el => el.validationMessage"
        )
    
    def first_urgent_event_type(self) -> str:
        """
        Return the type of the first displayed urgent event.
        """
        return self.first_text(self.map.URGENT_EVENT_TYPE)

    def first_urgent_event_time(self) -> str:
        """
        Return the time of the first displayed urgent event.
        """
        return self.first_text(self.map.URGENT_EVENT_TIME)

    def first_urgent_event_description(self) -> str:
        """
        Return the description of the first displayed urgent event.
        """
        return self.first_text(self.map.URGENT_EVENT_DESCRIPTION)
    
    def first_urgent_event_is_marked_red(self) -> bool:
        """
        Check if first urgent event has red styling.
        """
        classes = self.locator(self.map.URGENT_ITEMS).first.get_attribute("class")
        return "urgent-event-red" in (classes or "")

    # =========================
    # Events History - Actions
    # =========================

    def ensure_events_history_open(self):
        """
        Ensure that the events history section is open.
        If it is already visible, do nothing. Otherwise, open it.
        """
        if not self.is_visible(self.map.EVENTS_SECTION):
            self.click(self.map.VIEW_EVENTS_BTN)

    @allure.step("Open events history")
    def open_events_history(self):
        """
        Open events history section.
        """
        self.click(self.map.VIEW_EVENTS_BTN)

    # =====================================
    # Events History - Getters / Validations
    # =====================================

    def event_count(self) -> int:
        """
        Get number of events in history.
        """
        return self.count(self.map.EVENT_ROWS)
    
    def first_event_row_text(self) -> str:
        """
        Return full text of the first event row.
        """
        return self.first_text(self.map.EVENT_ROWS)
    
    def all_event_rows_text(self) -> list[str]:
        """
        Return text of all event rows.
        """
        return self.locator(self.map.EVENT_ROWS).all_inner_texts()
    
    def is_events_history_visible(self) -> bool:
        """
        Check if events history section is visible.
        """
        return self.is_visible(self.map.EVENTS_SECTION)

    def is_no_events_message_visible(self) -> bool:
        """
        Check if no events message is visible.
        """
        return self.is_visible(self.map.NO_EVENTS_MESSAGE)

    # ======================
    # User Actions
    # ======================
    
    @allure.step("Logout user")
    def logout(self):
        """
        Logout from the application.
        """
        self.click(self.map.LOGOUT)

    # ============================
    # User - Getters / Validations
    # ============================
    
    def get_logged_in_user(self) -> str:
        """
        Return the displayed logged-in username.
        """
        return self.text(self.map.USER)