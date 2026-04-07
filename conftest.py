import os
import pytest
import allure
from playwright.sync_api import sync_playwright
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.config import BASE_URL, SCREENSHOT_DIR


def pytest_addoption(parser):
    parser.addoption("--headed", action="store_true", default=False)


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture
def page(playwright_instance, pytestconfig, request):
    browser = playwright_instance.chromium.launch(
        headless=not pytestconfig.getoption("--headed"),
        slow_mo=1000 if pytestconfig.getoption("--headed") else 0,
    )
    context = browser.new_context()
    page = context.new_page()
    page.goto(BASE_URL)

    yield page

    context.close()
    browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Capture a screenshot and attach it to Allure when a test fails.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or report.passed:
        return

    page = item.funcargs.get("page")
    if page is None:
        return

    screenshots_dir = SCREENSHOT_DIR
    os.makedirs(screenshots_dir, exist_ok=True)

    test_name = item.name.replace("/", "_").replace("\\", "_").replace(":", "_")
    screenshot_path = os.path.join(screenshots_dir, f"{test_name}.png")

    page.screenshot(path=screenshot_path, full_page=True)

    allure.attach.file(
        screenshot_path,
        name=f"{test_name}_failure_screenshot",
        attachment_type=allure.attachment_type.PNG,
    )

@pytest.fixture
def logged_in_dashboard(page):
    """
    Fixture to log in and return the dashboard page object for tests.
    """
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    login_page.login("yoni", "1234")
    return dashboard_page