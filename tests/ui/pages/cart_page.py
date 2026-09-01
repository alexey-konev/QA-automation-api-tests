from tests.ui.components.header import Header
from tests.ui.pages.checkout_page import CheckoutPage


class CartPage:
    def __init__(self, page):
        self.page = page
        self.header = Header(page)

        self.checkout_button = self.page.get_by_role("button", name="Checkout")

    def open(self):
        self.page.goto("https://www.saucedemo.com/cart.html")

    def get_product_card(self, product_name):
        card = self.page.locator(".cart_item").filter(has=self.page.get_by_text(product_name))

        return card

    def remove_product(self, product_name):
        card = self.get_product_card(product_name)

        card.get_by_role("button", name="Remove").click()

    def start_checkout(self):
        self.checkout_button.click()

        return CheckoutPage(self.page)