"""
Stores and gives access to current instances of playwright objects
"""
from playwright.sync_api import sync_playwright, Page


class PlaywrightManager:
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
    PlaywrightManager.playwright_instance = sync_playwright().start()
    PlaywrightManager.browser = PlaywrightManager.playwright_instance.chromium.launch(headless=headless)
    PlaywrightManager.context = PlaywrightManager.browser.new_context()
    PlaywrightManager.context.set_default_timeout(5000)
    PlaywrightManager.page = PlaywrightManager.context.new_page()

def teardown_playwright():
    """
    Stops playwright
    """
    PlaywrightManager.context.close()
    PlaywrightManager.browser.close()
    PlaywrightManager.playwright_instance.stop()

def page() -> Page:
    """
    Returns a current instance of playwright page
    """
    return PlaywrightManager.page
