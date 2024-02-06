"""
Keywords for the *Sauce Demo* web app
"""
from playwright_manager import page, setup_playwright, teardown_playwright
from playwright.sync_api import expect
from robot.api import ContinuableFailure

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

def login(username, password):
    """
    Enters the credentials `username` and `password`
    and clicks _login_
    """
    username_input_field = page().locator("#user-name")
    username_input_field.fill(username)
    pass_input_field = page().locator("#password")
    pass_input_field.fill(password)
    page().locator("#login-button").click()

def check_backpack_shown(backpack_name):
    link_element = page().locator("#item_4_title_link")
    actual_value = link_element.inner_text()
    if backpack_name != actual_value:
        raise ContinuableFailure("Backpack is different, but go on")
    #expect(link_element).to_have_text(backpack_name)
