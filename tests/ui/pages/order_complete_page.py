from tests.ui.components.header import Header
from tests.ui.pages.base_page import BasePage


class OrderCompletePage(BasePage):
    path = "/checkout-complete.html"

    def __init__(self, page):
        super().__init__(page)

        self.header = Header(self.page)
        self.complete_message = self.page.get_by_text("Thank you for your order!")
        self.back_home_button = self.page.get_by_role("button", name="Back home")
