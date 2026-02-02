import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_management():
    browser.config.timeout = 10
    browser.driver.maximize_window()
    yield
    browser.quit()
