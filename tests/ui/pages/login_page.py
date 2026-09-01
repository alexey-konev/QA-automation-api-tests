from tests.ui.pages.inventory_page import InventoryPage


class LoginPage:
    def __init__(self, page):
        self.page = page

        self.username_input = self.page.get_by_placeholder("Username")
        self.password_input = self.page.get_by_placeholder("Password")
        self.login_button = self.page.locator("[data-test='login-button']")

    def open(self):
        self.page.goto("https://www.saucedemo.com")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

        return InventoryPage(self.page)
