"""
Stores and gives access to current instances of playwright objects
"""
from playwright.sync_api import sync_playwright, Page


class PageObject:
    """
    Keeps current instances of playwright objects
    """

    playwright_instance = None
    browser = None
    context = None
    page = None


def setup_playwright(headless=False):
    """
    Initializes playwright
    """
    PageObject.playwright_instance = sync_playwright().start()
    PageObject.browser = PageObject.playwright_instance.chromium.launch(
        headless=headless
    )
    PageObject.context = PageObject.browser.new_context()
    PageObject.context.set_default_timeout(5000)
    PageObject.page = PageObject.context.new_page()


def teardown_playwright():
    """
    Stops playwright
    """
    PageObject.context.close()
    PageObject.browser.close()
    PageObject.playwright_instance.stop()


def page() -> Page:
    """
    Returns a current instance of playwright page
    """
    return PageObject.page
