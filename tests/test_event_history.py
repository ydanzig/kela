"""
Event history-related tests.

Test Coverage:
- Total test functions: 9
- Total executed test cases: 10
- Skipped tests: 1

| Test Name                                           | Test Type              | Description                                                                 |
|-----------------------------------------------------|------------------------|-----------------------------------------------------------------------------|
| test_open_events_history_success                    | Positive, Sanity       | Verify that the events history section can be opened successfully           |
| test_events_history_empty_state                     | Positive               | Verify that empty state is displayed when no events exist                   |
| test_task_creation_adds_event_to_history            | Positive               | Verify that creating a task adds an entry to events history                 |
| test_urgent_event_creation_adds_event_to_history    | Positive, Parametrized | Verify that creating an urgent event adds an entry to events history        |
| test_events_history_order_latest_first              | State                  | Verify that the latest event appears first in history                       |
| test_urgent_event_order_latest_first                | State, Skipped         | Verify that the latest urgent event appears first in history                |
| test_multiple_task_creations_add_multiple_events_to_history | State          | Verify that creating multiple tasks adds multiple entries to events history |
| test_mixed_events_are_logged_in_history             | State                  | Verify that both task events and urgent events are logged in history        |
| test_task_deletion_does_not_remove_event_from_history | State                | Verify that deleting a task does not remove its creation event from history |
"""

import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def login_as_valid_user(page):
    LoginPage(page).login("yoni", "1234")


############################################################################################
######################################## Positive Tests ####################################
############################################################################################

@pytest.mark.history
@pytest.mark.sanity
@pytest.mark.positive
def test_open_events_history_success(page):
    """
    Verify that the events history section can be opened successfully.
    """
    login_as_valid_user(page)
    dashboard = DashboardPage(page)

    dashboard.open_events_history()

    assert dashboard.is_visible(dashboard.EVENTS_SECTION), \
        "Expected events history section to be visible after opening."


@pytest.mark.history
@pytest.mark.positive
def test_events_history_empty_state(page):
    """
    Verify that empty state is displayed when no events exist.
    """
    login_as_valid_user(page)
    dashboard = DashboardPage(page)

    dashboard.ensure_events_history_open()

    assert dashboard.is_visible(dashboard.NO_EVENTS_MESSAGE), \
        "Expected no-events message when history is empty."

    assert dashboard.event_count() == 0, \
        f"Expected 0 events in history, but found {dashboard.event_count()}."


@pytest.mark.history
@pytest.mark.positive
def test_task_creation_adds_event_to_history(page):
    """
    Verify that creating a task adds an entry to events history.
    """
    login_as_valid_user(page)
    dashboard = DashboardPage(page)

    task_name = "history_test_task"

    dashboard.add_task(task_name)
    dashboard.ensure_events_history_open()

    assert dashboard.event_count() == 1, \
        f"Expected 1 event in history after task creation, but found {dashboard.event_count()}."

    assert task_name in dashboard.first_event_row_text(), \
        f"Created task name - {task_name} was not found in events history entry."


@pytest.mark.history
@pytest.mark.positive
@pytest.mark.parametrize(
    "urgent_bool",
    [True, False],
    ids=["marked_urgent", "not_marked_urgent"],
)
def test_urgent_event_creation_adds_event_to_history(page, urgent_bool):
    """
    Verify that creating an urgent event adds an entry to events history.
    """
    login_as_valid_user(page)
    dashboard = DashboardPage(page)

    dashboard.add_urgent_event("attack", "20:00", "critical", urgent=urgent_bool)
    dashboard.ensure_events_history_open()

    assert dashboard.event_count() == 1, \
        f"Expected 1 event in history after urgent event creation, but found {dashboard.event_count()}."

    first_row_text = dashboard.first_event_row_text()

    assert "attack" in first_row_text.lower(), \
        f"Urgent event was not found in events history. Got: {first_row_text}"


############################################################################################
######################################## State Tests #######################################
############################################################################################

@pytest.mark.history
@pytest.mark.state
def test_events_history_order_latest_first(page):
    """
    Verify that the latest event appears first in history.
    """
    login_as_valid_user(page)
    dashboard = DashboardPage(page)

    dashboard.add_task("first_history_task")
    dashboard.add_task("second_history_task")

    dashboard.ensure_events_history_open()

    assert dashboard.event_count() == 2, \
        f"Expected 2 events in history, but found {dashboard.event_count()}."

    assert "second_history_task" in dashboard.first_event_row_text(), \
        "Latest event is not displayed first in events history."

@pytest.mark.history
@pytest.mark.state
@pytest.mark.skip(reason="BUG: urgent events are not appearing in events history list")
def test_urgent_event_order_latest_first(page):
    """
    Verify that the latest urgent event appears first in history.
    (Currently skipped due to known bug)
    """
    login_as_valid_user(page)
    dashboard = DashboardPage(page)

    dashboard.add_urgent_event("attack", description="first urgent", urgent=True)
    dashboard.add_urgent_event("breach", description="second urgent", urgent=True)

    dashboard.ensure_events_history_open()

    assert dashboard.event_count() == 2, \
        f"Expected 2 events in history, but found {dashboard.event_count()}."

    assert "second urgent" in dashboard.first_event_row_text(), \
        "Latest urgent event is not displayed first in events history."
    

@pytest.mark.history
@pytest.mark.state
def test_multiple_task_creations_add_multiple_events_to_history(page):
    """
    Verify that creating multiple tasks adds multiple entries to events history.
    """
    login_as_valid_user(page)
    dashboard = DashboardPage(page)

    first_task_name = "history_task_one"
    second_task_name = "history_task_two"

    dashboard.add_task(first_task_name)
    dashboard.add_task(second_task_name)

    dashboard.ensure_events_history_open()

    assert dashboard.event_count() == 2, \
        f"Expected 2 events in history after creating two tasks, but found {dashboard.event_count()}."

    all_rows_text = dashboard.all_event_rows_text()

    assert any(first_task_name in row for row in all_rows_text), \
        f"First created task '{first_task_name}' was not found in events history. Got: {all_rows_text}"

    assert any(second_task_name in row for row in all_rows_text), \
        f"Second created task '{second_task_name}' was not found in events history. Got: {all_rows_text}"
    
@pytest.mark.history
@pytest.mark.state
def test_mixed_events_are_logged_in_history(page):
    """
    Verify that both task events and urgent events are logged in events history.
    """
    login_as_valid_user(page)
    dashboard = DashboardPage(page)

    task_name = "mixed_history_task"
    urgent_description = "mixed urgent event"


    dashboard.add_task(task_name)
    dashboard.add_urgent_event("attack", "20:00", urgent_description, urgent=True)

    dashboard.ensure_events_history_open()

    assert dashboard.event_count() == 2, \
        f"Expected 2 events in history, but found {dashboard.event_count()}."

    all_rows_text = dashboard.all_event_rows_text()

    assert any(task_name in row for row in all_rows_text), \
        f"Task event '{task_name}' was not found in events history. Got: {all_rows_text}"

    assert any("attack" in row.lower() for row in all_rows_text), \
        f"Urgent event was not found in events history. Got: {all_rows_text}"
    

@pytest.mark.history
@pytest.mark.state
def test_task_deletion_does_not_remove_event_from_history(page):
    """
    Verify that deleting a task does not remove its creation event from history.
    """
    login_as_valid_user(page)
    dashboard = DashboardPage(page)

    task_name = "task_for_history_test"

    # Create task
    dashboard.add_task(task_name)

    # Open history and verify creation event exists
    dashboard.ensure_events_history_open()

    all_rows = dashboard.all_event_rows_text()
    assert any(task_name in row for row in all_rows), \
        f"Task creation event not found in history. Got: {all_rows}"

    # Delete task
    dashboard.delete_first_task()

    assert dashboard.task_count() == 0, \
        "Task was not deleted from tasks list."

    # Verify history still contains the event
    all_rows = dashboard.all_event_rows_text()
    assert any(task_name in row for row in all_rows), \
        f"Task creation event was removed from history after deletion. Got: {all_rows}"