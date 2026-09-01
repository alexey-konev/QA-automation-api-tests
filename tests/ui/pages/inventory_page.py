from tests.ui.components.header import Header
from tests.ui.pages.cart_page import CartPage


class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.header = Header(page)

    def open(self):
        self.page.goto("https://www.saucedemo.com/inventory.html")

    def get_product_card(self, product_name):
        card = self.page.locator(".inventory_item").filter(has=self.page.get_by_text(product_name))

        return card

    def add_product(self, product_name):
        card = self.get_product_card(product_name)

        card.get_by_role("button", name="Add to cart").click()

    def open_cart(self):
        self.header.open_cart()

        return CartPage(self.page)