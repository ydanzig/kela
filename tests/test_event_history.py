from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def login_as_valid_user(page):
    LoginPage(page).login("yoni", "1234")


def test_task_creation_adds_event_to_history(page):
    login_as_valid_user(page)
    dashboard = DashboardPage(page)

    dashboard.add_task("My first task")
    dashboard.open_events_history()

    assert page.locator(dashboard.EVENTS_SECTION).is_visible()
    assert dashboard.event_count() == 1
    assert 'My first task' in page.locator(dashboard.EVENT_ROWS).first.inner_text()


def test_events_history_empty_state(page):
    login_as_valid_user(page)
    dashboard = DashboardPage(page)

    dashboard.open_events_history()

    assert page.locator(dashboard.NO_EVENTS_MESSAGE).is_visible()