from tests.ui.components.header import Header
from tests.ui.pages.order_complete_page import OrderCompletePage


class CheckoutOverviewPage:
    def __init__(self, page):
        self.page = page
        self.header = Header(page)

        self.finish_button = self.page.get_by_role("button", name="Finish")

    def open(self):
        self.page.goto("https://www.saucedemo.com/checkout-step-two.html")

    def get_product_card(self, product_name):
        card = self.page.locator(".cart_item").filter(has=self.page.get_by_text(product_name))

        return card

    def finish_checkout(self):
        self.finish_button.click()

        return OrderCompletePage(self.page)

