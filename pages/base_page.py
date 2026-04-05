from playwright.sync_api import Page, Locator


class BasePage:
    """
    Base page abstraction for all page objects in the framework.

    This class provides reusable wrapper methods around common Playwright
    actions in order to reduce code duplication and improve maintainability.
    """

    def __init__(self, page: Page):
        """
        Initialize the page object.

        :param page: Playwright Page instance.
        """
        self.page = page

    def locator(self, selector: str) -> Locator:
        """
        Return a Playwright locator for the given selector.

        :param selector: CSS selector or data-testid selector.
        :return: Playwright Locator object.
        """
        return self.page.locator(selector)

    def click(self, selector: str):
        """
        Click on an element.

        :param selector: CSS selector or data-testid selector.
        """
        self.locator(selector).click()

    def fill(self, selector: str, value: str):
        """
        Fill an input field.

        :param selector: CSS selector or data-testid selector.
        :param value: Text value to enter.
        """
        self.locator(selector).fill(value)

    def text(self, selector: str) -> str:
        """
        Get the inner text of an element.

        :param selector: CSS selector or data-testid selector.
        :return: Element text.
        """
        return self.locator(selector).inner_text()

    def is_visible(self, selector: str) -> bool:
        """
        Check whether an element is visible.

        :param selector: CSS selector or data-testid selector.
        :return: True if visible, otherwise False.
        """
        return self.locator(selector).is_visible()