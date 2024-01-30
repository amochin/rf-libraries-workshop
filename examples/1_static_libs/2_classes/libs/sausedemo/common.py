"""
Common keywords for the *Sauce Demo" web app
"""
from .page_object import page, setup_playwright, teardown_playwright

BASE_URL = "https://www.saucedemo.com/"

def launch_sausedemo():
    """
    Opens the start page of SauseDemo
    """
    setup_playwright(headless=False)
    page().goto(BASE_URL)

def close_sausedemo():
    """
    Closes the browser
    """
    teardown_playwright()
