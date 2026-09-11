from playwright.sync_api import expect

from tests.ui.config import BASE_URL
from tests.ui.data.customers import VALID_CUSTOMER
from tests.ui.data.products import PRODUCTS
from tests.ui.data.users import STANDARD_USER


def test_add_product_to_cart(inventory_page):
    inventory_page.open()
    inventory_page.add_product(PRODUCTS["backpack"])

    expect(inventory_page.header.cart_badge).to_have_text("1")


def test_add_multiple_products_to_cart(inventory_page):
    product_list = [PRODUCTS["backpack"], PRODUCTS["bike_light"], PRODUCTS["tshirt"]]

    inventory_page.open()
    for item in product_list:
        inventory_page.add_product(item)

    expect(inventory_page.header.cart_badge).to_have_text("3")

    cart_page = inventory_page.open_cart()

    for item in product_list:
        expect(cart_page.get_product_card(item)).to_be_visible()


def test_remove_single_product_from_cart(inventory_page):
    inventory_page.open()
    inventory_page.add_product(PRODUCTS["backpack"])
    cart_page = inventory_page.open_cart()

    expect(cart_page.get_product_card(PRODUCTS["backpack"])).to_be_visible()

    cart_page.remove_product(PRODUCTS["backpack"])

    expect(cart_page.get_product_card(PRODUCTS["backpack"])).to_have_count(0)
    expect(cart_page.header.cart_badge).to_be_hidden()


def test_remove_one_out_of_two_products_from_cart(inventory_page):
    inventory_page.open()
    inventory_page.add_product(PRODUCTS["backpack"])
    inventory_page.add_product(PRODUCTS["bike_light"])
    cart_page = inventory_page.open_cart()

    expect(cart_page.get_product_card(PRODUCTS["backpack"])).to_be_visible()
    expect(cart_page.get_product_card(PRODUCTS["bike_light"])).to_be_visible()

    cart_page.remove_product(PRODUCTS["backpack"])

    expect(cart_page.get_product_card(PRODUCTS["backpack"])).to_have_count(0)
    expect(cart_page.get_product_card(PRODUCTS["bike_light"])).to_have_count(1)
    expect(cart_page.header.cart_badge).to_have_text("1")


def test_successful_purchase(login_page):
    login_page.open()

    inventory_page = login_page.login(STANDARD_USER["login"], STANDARD_USER["password"])
    inventory_page.add_product(PRODUCTS["backpack"])
    expect(inventory_page.header.cart_badge).to_have_text("1")

    cart_page = inventory_page.open_cart()
    expect(cart_page.get_product_card(PRODUCTS["backpack"])).to_be_visible()

    checkout_page = cart_page.start_checkout()
    checkout_page.fill_customer_info(VALID_CUSTOMER["firstname"], VALID_CUSTOMER["lastname"], VALID_CUSTOMER["code"])

    checkout_overview_page = checkout_page.continue_checkout()
    expect(checkout_overview_page.get_product_card(PRODUCTS["backpack"])).to_be_visible()

    order_complete_page = checkout_overview_page.finish_checkout()
    expect(order_complete_page.page).to_have_url(f"{BASE_URL}/checkout-complete.html")
    expect(order_complete_page.complete_message).to_be_visible()

