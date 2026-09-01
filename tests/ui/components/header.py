class Header:
    def __init__(self, page):
        self.page = page

        self.cart_link = self.page.locator(".shopping_cart_link")
        self.cart_badge = self.page.locator(".shopping_cart_badge")
        self.burger_menu_button = self.page.get_by_role("button", name="Open Menu")

    def open_cart(self):
        self.cart_link.click()
