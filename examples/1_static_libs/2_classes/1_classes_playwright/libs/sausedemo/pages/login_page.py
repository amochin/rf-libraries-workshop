from ..playwright_manager import page

class LoginPage:
    def login(self, username, password):
        username_input_field = page().locator("#user-name")
        username_input_field.fill(username)
        pass_input_field = page().locator("#password")
        pass_input_field.fill(password)
        page().locator("#login-button").click()
    