from playwright.sync_api import expect

from tests.ui.data.users import STANDARD_USER


def test_successful_login(login_page, base_url):

    login_page.open()
    inventory_page = login_page.login(STANDARD_USER["login"], STANDARD_USER["password"])

    expect(inventory_page.page).to_have_url(f"{base_url}/inventory.html")

    title = inventory_page.title
    expect(title).to_be_visible()
    expect(title).to_have_text("Products")



