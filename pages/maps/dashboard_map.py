class DashboardMap():
    """
    Map class for the Dashboard Page. Contains locators for all elements on the dashboard page.
    """
    
    # ===========================
    # Locators for Dashboard Page
    # ===========================
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