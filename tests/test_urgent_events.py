"""
Urgent event-related tests covering creation, validation, display, and deletion flows.

Test Coverage:
- Total test functions: 6
- Total executed test cases: 12

| Test Name                                     | Test Type                     | Description                                                               |
|-----------------------------------------------|-------------------------------|---------------------------------------------------------------------------|
| test_add_attack_urgent_event_success          | Positive, Sanity              | Verify adding a basic urgent attack event successfully                    |
| test_add_urgent_event_displays_values_for_each_type | Positive, Parametrized  | Verify correct display of type, time, description, and styling            |
| test_add_urgent_event_without_type            | Negative, Parametrized        | Verify that event type is required for urgent event creation              |
| test_delete_urgent_event                      | State, Sanity                 | Verify deleting an existing urgent event                                  |
| test_delete_one_of_multiple_urgent_events     | State                         | Verify deleting one urgent event out of multiple existing events          |
| test_delete_all_urgent_events_one_by_one      | State                         | Verify deleting all urgent events sequentially until the list is empty    |
"""

import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from tests.expected import UrgentEventExpected

def login_as_valid_user(page):
    LoginPage(page).login("yoni", "1234")

############################################################################################
######################################## Positive Tests ####################################
############################################################################################

@pytest.mark.urgent
@pytest.mark.sanity
@pytest.mark.positive
def test_add_attack_urgent_event_success(page):
    """
    Verify that an attack urgent event can be added successfully.
    """
    login_as_valid_user(page)
    dashboard = DashboardPage(page)

    dashboard.add_urgent_event("attack", "20:00", "Critical issue", urgent=True)

    assert dashboard.urgent_event_count() == 1, \
        f"Expected 1 urgent event, but found {dashboard.urgent_event_count()}."

    assert dashboard.first_urgent_event_type() == UrgentEventExpected.ATTACK_EVENT_TEXT, \
        f"Urgent event type is not displayed correctly. Expected {UrgentEventExpected.ATTACK_EVENT_TEXT} but got '{dashboard.first_urgent_event_type()}'."
   
@pytest.mark.urgent
@pytest.mark.positive
@pytest.mark.parametrize(
    "event_type, expected_text",
    [
        ("attack", UrgentEventExpected.ATTACK_EVENT_TEXT),
        ("assault", UrgentEventExpected.ASSAULT_EVENT_TEXT),
        ("breach", UrgentEventExpected.BREACH_EVENT_TEXT),
        ("red", UrgentEventExpected.RED_EVENT_TEXT),
    ],
    ids=[
        "attack_type",
        "assault_type",
        "breach_type",
        "red_type",
    ],
)
@pytest.mark.parametrize(
    "urgent_bool",
    [True, False],
    ids=["marked_urgent", "not_marked_urgent"],
)
def test_add_urgent_event_displays_values_for_each_type(page, event_type, expected_text, urgent_bool):
    """
    Verify that entered values are correctly displayed for each urgent event type.
    We also check that the card color is red when marked urgent, and not red when not marked urgent.
    """
    login_as_valid_user(page)
    dashboard = DashboardPage(page)

    event_time = "20:00"
    description = f"{expected_text} description"

    dashboard.add_urgent_event(
        event_type=event_type,
        time=event_time,
        description=description,
        urgent=urgent_bool,
    )

    assert dashboard.urgent_event_count() == 1, \
        f"Expected 1 urgent event, but found {dashboard.urgent_event_count()}."

    assert dashboard.first_urgent_event_type() == expected_text, \
        f"Event type mismatch: expected '{expected_text}', got '{dashboard.first_urgent_event_type()}'."

    assert dashboard.first_urgent_event_time() == event_time, \
        f"Event time mismatch: expected '{event_time}', got '{dashboard.first_urgent_event_time()}'."

    assert dashboard.first_urgent_event_description() == description, \
        f"Event description mismatch: expected '{description}', got '{dashboard.first_urgent_event_description()}'."
    
    assert dashboard.first_urgent_event_is_marked_red() == urgent_bool, \
        f"Urgent event red styling mismatch: expected red={urgent_bool}, got red={dashboard.first_urgent_event_is_marked_red()}."

############################################################################################
######################################## Negative Tests ####################################
############################################################################################

@pytest.mark.urgent
@pytest.mark.negative
@pytest.mark.parametrize(
    "urgent_bool",
    [True, False],
    ids=["without_type_marked_urgent", "without_type_not_marked_urgent"],
)
def test_add_urgent_event_without_type(page, urgent_bool):
    """
    Verify that urgent event cannot be created without selecting event type.
    """
    login_as_valid_user(page)
    dashboard = DashboardPage(page)

    dashboard.add_urgent_event(
        event_type="",
        time="12:00",
        description="Missing type",
        urgent=urgent_bool,
    )

    assert dashboard.urgent_event_count() == 0, \
        f"Urgent event was created without selecting event type. Found {dashboard.urgent_event_count()} events."


    assert dashboard.is_urgent_type_select_invalid(), (
        "Expected event type select to be invalid when no option is selected."
    )

    assert dashboard.urgent_type_validation_message() == UrgentEventExpected.PLEASE_SELECT_ITEM, (
        f"Unexpected validation message: {dashboard.urgent_type_validation_message()}"
    )

############################################################################################
######################################## State Tests #######################################
############################################################################################

@pytest.mark.sanity
@pytest.mark.urgent
@pytest.mark.state
def test_delete_urgent_event(page):
    """
    Verify that an existing urgent event can be deleted successfully.
    """
    login_as_valid_user(page)
    dashboard = DashboardPage(page)

    dashboard.add_urgent_event("breach")

    assert dashboard.urgent_event_count() == 1, \
        "Precondition failed: expected one urgent event before deletion."

    dashboard.delete_first_urgent_event()

    assert dashboard.urgent_event_count() == 0, \
        "Expected no urgent events after deletion."

@pytest.mark.urgent
@pytest.mark.state
def test_delete_one_of_multiple_urgent_events(page):
    """
    Verify deleting one urgent event when multiple events exist.
    """
    login_as_valid_user(page)
    dashboard = DashboardPage(page)

    dashboard.add_urgent_event("attack")
    dashboard.add_urgent_event("breach")

    assert dashboard.urgent_event_count() == 2, \
        "Precondition failed: expected two urgent events before deletion."

    dashboard.delete_first_urgent_event()

    assert dashboard.urgent_event_count() == 1, \
        "Expected one urgent event after deleting one."
    
@pytest.mark.urgent
@pytest.mark.state
def test_delete_all_urgent_events_one_by_one(page):
    """
    Verify that all urgent events can be deleted one by one until none remain.
    """
    login_as_valid_user(page)
    dashboard = DashboardPage(page)

    event_types = ["attack", "assault", "breach", "red"]

    # Add multiple urgent events
    for event_type in event_types:
        dashboard.add_urgent_event(event_type)

    assert dashboard.urgent_event_count() == len(event_types), \
        f"Precondition failed: expected {len(event_types)} urgent events before deletion, but found {dashboard.urgent_event_count()}."

    # Delete all events one by one
    remaining = len(event_types)

    while remaining > 0:
        dashboard.delete_first_urgent_event()
        remaining -= 1

        assert dashboard.urgent_event_count() == remaining, \
            f"Expected {remaining} urgent events remaining after deletion, but found {dashboard.urgent_event_count()}."
    
    assert dashboard.urgent_event_count() == 0, \
        "Expected no urgent events remaining after deleting all."