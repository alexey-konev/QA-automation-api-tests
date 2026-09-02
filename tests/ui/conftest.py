import pytest
from playwright.sync_api import expect

from tests.ui.config import BASE_URL
from tests.ui.pages.inventory_page import InventoryPage
from tests.ui.pages.login_page import LoginPage


@pytest.fixture(scope="session")
def auth_state(browser):
    context = browser.new_context(
        base_url=BASE_URL
    )
    page = context.new_page()

    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(f"{BASE_URL}/inventory.html")

    context.storage_state(path="auth.json")

    context.close()


@pytest.fixture()
def authenticated_page(browser, auth_state):
    context = browser.new_context(
        base_url=BASE_URL,
        storage_state="auth.json"
    )
    page = context.new_page()

    yield page

    context.close()


@pytest.fixture()
def inventory_page(authenticated_page):
    return InventoryPage(authenticated_page)


@pytest.fixture()
def login_page(browser):
    context = browser.new_context(
        base_url=BASE_URL
    )
    page = context.new_page()

    yield LoginPage(page)

    context.close()