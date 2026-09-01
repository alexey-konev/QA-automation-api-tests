from tests.ui.components.header import Header


class OrderCompletePage:
    def __init__(self, page):
        self.page = page
        self.header = Header(page)

        self.complete_message = self.page.get_by_text("Thank you for your order!")
        self.back_home_button = self.page.get_by_role("button", name="Back home")


    def open(self):
        self.page.goto("https://www.saucedemo.com/checkout-complete.html")