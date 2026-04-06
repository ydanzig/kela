"""
Task-related tests.

Test Coverage:
- Total test functions: 6
- Total executed test cases: 11

| Test Name                                  | Test Type                     | Description                                                  |
|--------------------------------------------|-------------------------------|--------------------------------------------------------------|
| test_add_task_success                      | Positive, Parametrized        | Verify adding a task with all fields populated               |
| test_add_task_with_default_optional_values | Positive, Parametrized        | Verify adding a task with only required fields               |
| test_add_duplicate_task_allowed            | Edge, State                   | Verify that duplicate tasks can be added and both exist      |
| test_delete_task                           | State                         | Verify deleting an existing task                             |
| test_add_many_tasks                        | Stress                        | Verify that the system can handle adding multiple tasks      |
| test_add_task_with_invalid_name            | Negative, Parametrized        | Verify that a task cannot be created with an invalid name    |
"""

import pytest
from tests.expected import TaskExpected
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import NUM_TASKS

############################################################################################
######################################## Positive/edge Tests ###############################
############################################################################################

@pytest.mark.tasks
@pytest.mark.positive
@pytest.mark.parametrize(
    "username, password, task_name, task_time, task_description",
    [
        ("yoni", "1234", "Buy milk", "18:00", "From supermarket"),
        ("yoni", "1234", "Call mom", "09:30", "Weekly reminder"),
        ("yoni", "1234", "Team meeting", "14:15", "Discuss sprint progress"),
    ],
    ids=[
        "add_task_with_evening_time",
        "add_task_with_morning_time",
        "add_task_with_work_description",
    ],
)
def test_add_task_success(page, username, password, task_name, task_time, task_description):
    """
    Verify that a new task can be added successfully with all fields populated.
    """
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.login(username, password)
    dashboard_page.add_task(task_name, task_time, task_description)

    assert dashboard_page.task_count() == 1, \
        "Expected exactly one task to be displayed after adding a task."

    assert dashboard_page.first_task_name() == task_name, \
        "The displayed task name does not match the created task."
    
    assert dashboard_page.first_task_time() == task_time, \
        "The displayed task time does not match the created task."

    assert dashboard_page.first_task_description() == task_description, \
        "The displayed task description does not match the created task."

@pytest.mark.tasks
@pytest.mark.positive
@pytest.mark.parametrize(
    "username, password, task_name",
    [
        ("yoni", "1234", "Read book it's good for your brain!"),
        ("yoni", "1234", "Workout! you can do it!"),
        ("yoni", "1234", "Pay bills on time, don't forget!"),
    ],
    ids=[
        "add_task_with_required_field_only_read_book",
        "add_task_with_required_field_only_workout",
        "add_task_with_required_field_only_pay_bills",
    ],
)
def test_add_task_with_default_optional_values(page, username, password, task_name):
    """
    Verify task creation when only the required task name field is provided.
    """
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.login(username, password)
    dashboard_page.add_task(task_name)

    assert dashboard_page.task_count() == 1, \
        f"Expected one task to be displayed after adding a task with only required fields., but found {dashboard_page.task_count()}."

    assert dashboard_page.first_task_name() == task_name, \
        f"The displayed task name does not match the created task. expected '{task_name}' but got '{dashboard_page.first_task_name()}'."

    assert dashboard_page.first_task_time() == TaskExpected.DEFAULT_TIME, \
        f"Unexpected default task time value expected {TaskExpected.DEFAULT_TIME} but got {dashboard_page.first_task_time()}."

    assert dashboard_page.first_task_description() == TaskExpected.DEFAULT_DESCRIPTION, \
        f"Unexpected default task description value expected {TaskExpected.DEFAULT_DESCRIPTION} but got {dashboard_page.first_task_description()}."

@pytest.mark.tasks
@pytest.mark.edge
@pytest.mark.state
def test_add_duplicate_task_allowed(page):
    """
    Verify that adding the same task twice results in two separate tasks.
    """
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.login("yoni", "1234")

    task_name = "Duplicate Task"
    task_time = "12:00"
    task_description = "Same task twice"

    # Add the same task twice
    dashboard_page.add_task(task_name, task_time, task_description)
    dashboard_page.add_task(task_name, task_time, task_description)

    # Verify both tasks exist
    assert dashboard_page.task_count() == 2, \
        f"Expected 2 tasks after adding duplicate task, but found {dashboard_page.task_count()}."
    
############################################################################################
######################################## Negative Tests ####################################
############################################################################################

@pytest.mark.tasks
@pytest.mark.negative
@pytest.mark.parametrize(
    "task_name",
    ["", "   "],
    ids=[
        "empty_task_name",
        "task_name_only_spaces",
    ],
)
def test_add_task_with_invalid_name(page, task_name):
    """
    Verify that a task cannot be created with an empty or invalid name.
    """
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.login("yoni", "1234")

    initial_count = dashboard_page.task_count()

    dashboard_page.add_task(task_name)

    assert dashboard_page.task_count() == initial_count, \
        "Task should not be created with invalid name."


############################################################################################
######################################## State Tests #######################################
############################################################################################

@pytest.mark.tasks
@pytest.mark.state
@pytest.mark.parametrize(
    "username, password, task_name",
    [
        ("yoni", "1234", "Task to delete"),
    ],
    ids=[
        "delete_existing_task",
    ],
)
def test_delete_task(page, username, password, task_name):
    """
    Verify that an existing task can be deleted successfully.
    """
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.login(username, password)
    dashboard_page.add_task(task_name)

    assert dashboard_page.task_count() == 1, \
        "Precondition failed: expected one task before deletion."

    dashboard_page.delete_first_task()

    assert dashboard_page.task_count() == 0, \
        "Expected no tasks to remain after deleting the only task."
    

    
############################################################################################
######################################## Stress Tests ######################################
############################################################################################
@pytest.mark.tasks
@pytest.mark.stress
def test_add_many_tasks(page):
    """
    Verify that the system can handle adding multiple tasks (stress scenario).
    """
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.login("yoni", "1234")

    number_of_tasks = NUM_TASKS

    for i in range(number_of_tasks):
        dashboard_page.add_task(f"Task {i}", "10:00", "Stress test")

    assert dashboard_page.task_count() == number_of_tasks, \
        f"Expected {number_of_tasks} tasks, but found {dashboard_page.task_count()}."
    
    assert dashboard_page.first_task_name() == f"Task {number_of_tasks - 1}", \
        "Latest created task is not displayed first as expected."