from playwright.sync_api import expect

from tests.ui.config import username, password


def test_successful_login(login_page, base_url):

    login_page.open()
    inventory_page = login_page.login(username, password)

    expect(inventory_page.page).to_have_url(f"{base_url}/inventory.html")

    title = inventory_page.title
    expect(title).to_be_visible()
    expect(title).to_have_text("Products")



