import pytest
from playwright.sync_api import expect

from tests.ui.config import ENVIRONMENTS
from tests.ui.pages.inventory_page import InventoryPage
from tests.ui.pages.login_page import LoginPage


#env
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="default"
    )

@pytest.fixture(scope="session")
def environment(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def base_url(environment):
    if environment not in ENVIRONMENTS:
        raise ValueError("Unknown environment")

    return ENVIRONMENTS[environment]


#pages
@pytest.fixture(scope="session")
def auth_state(browser, base_url):
    context = browser.new_context(
        base_url=base_url
    )
    page = context.new_page()

    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(f"{base_url}/inventory.html")

    storage_state = context.storage_state()

    context.close()

    return storage_state


@pytest.fixture()
def authenticated_page(browser, auth_state, base_url):
    context = browser.new_context(
        base_url=base_url,
        storage_state=auth_state
    )
    page = context.new_page()

    yield page

    context.close()


@pytest.fixture()
def inventory_page(authenticated_page):
    return InventoryPage(authenticated_page)


@pytest.fixture()
def login_page(browser, base_url):
    context = browser.new_context(
        base_url=base_url
    )
    page = context.new_page()

    yield LoginPage(page)

    context.close()