from typing import Generator, Any
import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page

@pytest.fixture(scope="session")
def browser() -> Generator[Browser, None, None]:
    chrome_options = [
        "--window-size=1920,1080"
    ]
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=chrome_options)
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Generator[Page, None, None]:
    page = context.new_page()
    yield page
    page.close()


