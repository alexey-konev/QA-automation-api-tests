from playwright.sync_api import expect


def test_successful_login(login_page):

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")

    title = login_page.page.locator("[data-test='title']")
    expect(title).to_be_visible()
    expect(title).to_have_text("Products")



