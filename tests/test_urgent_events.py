from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def login_as_valid_user(page):
    LoginPage(page).login("yoni", "1234")


def test_add_urgent_event_success(page):
    login_as_valid_user(page)
    dashboard = DashboardPage(page)

    dashboard.add_urgent_event("attack", "20:00", "Critical issue", urgent=True)

    assert dashboard.urgent_event_count() == 1
    item = page.locator(dashboard.URGENT_ITEMS).first
    assert item.locator('[data-testid="urgent-event-type"]').inner_text() == "Attack event"


def test_delete_urgent_event(page):
    login_as_valid_user(page)
    dashboard = DashboardPage(page)

    dashboard.add_urgent_event("breach")
    assert dashboard.urgent_event_count() == 1

    page.locator(dashboard.DELETE_URGENT_BTNS).first.click()

    assert dashboard.urgent_event_count() == 0