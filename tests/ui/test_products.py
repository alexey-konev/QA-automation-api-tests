from playwright.sync_api import expect

from tests.ui.conftest import inventory_page


def test_add_product_to_cart(inventory_page):
    inventory_page.open()
    inventory_page.add_product("Sauce Labs Backpack")

    expect(inventory_page.header.cart_badge).to_have_text("1")


def test_add_multiple_products_to_cart(inventory_page):
    product_list = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"]

    inventory_page.open()
    for item in product_list:
        inventory_page.add_product(item)

    expect(inventory_page.header.cart_badge).to_have_text("3")

    cart_page = inventory_page.open_cart()

    for item in product_list:
        expect(cart_page.get_product_card(item)).to_be_visible()


def test_remove_single_product_from_cart(inventory_page):
    inventory_page.open()
    inventory_page.add_product("Sauce Labs Backpack")
    cart_page = inventory_page.open_cart()

    expect(cart_page.get_product_card("Sauce Labs Backpack")).to_be_visible()

    cart_page.remove_product("Sauce Labs Backpack")

    expect(cart_page.get_product_card("Sauce Labs Backpack")).to_have_count(0)
    expect(cart_page.header.cart_badge).to_be_hidden()


def test_remove_one_out_of_two_products_from_cart(inventory_page):
    inventory_page.open()
    inventory_page.add_product("Sauce Labs Backpack")
    inventory_page.add_product("Sauce Labs Bike Light")
    cart_page = inventory_page.open_cart()

    expect(cart_page.get_product_card("Sauce Labs Backpack")).to_be_visible()
    expect(cart_page.get_product_card("Sauce Labs Bike Light")).to_be_visible()

    cart_page.remove_product("Sauce Labs Backpack")

    expect(cart_page.get_product_card("Sauce Labs Backpack")).to_have_count(0)
    expect(cart_page.get_product_card("Sauce Labs Bike Light")).to_have_count(1)
    expect(cart_page.header.cart_badge).to_have_text("1")


def test_successful_purchase(login_page):
    login_page.open()

    inventory_page = login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product("Sauce Labs Backpack")
    expect(inventory_page.header.cart_badge).to_have_text("1")

    cart_page = inventory_page.open_cart()
    expect(cart_page.get_product_card("Sauce Labs Backpack")).to_be_visible()

    checkout_page = cart_page.start_checkout()
    checkout_page.fill_customer_info("Name", "Lastname", "Code123")

    checkout_overview_page = checkout_page.continue_checkout()
    expect(checkout_overview_page.get_product_card("Sauce Labs Backpack")).to_be_visible()

    order_complete_page = checkout_overview_page.finish_checkout()
    expect(order_complete_page.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(order_complete_page.complete_message).to_be_visible()

