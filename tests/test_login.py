from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from pathlib import Path
import os
from pages.login_page import LoginPage


def test_login_page_title():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        login_page = LoginPage(page)

        login_page.navigate()

        assert "Log In" in page.title()

        browser.close()


def test_login_page_url():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        login_page = LoginPage(page)

        login_page.navigate()

        assert "identity.hudl.com/u/login" in page.url

        browser.close()


def test_empty_email():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        login_page = LoginPage(page)

        login_page.navigate()

        page.locator('button[type="submit"]').click()

        assert page.locator("text=Please enter your email address").first.is_visible()

        browser.close()


def test_empty_password():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        login_page = LoginPage(page)

        login_page.navigate()

        login_page.login("test@email.com", "")

        assert page.locator("text=Please enter your password").is_visible()

        browser.close()


def test_invalid_login():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login("fake@email.com", "fake1234")

        assert login_page.is_error_message_visible()

        browser.close()


def test_forgot_password_link():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        login_page = LoginPage(page)

        login_page.navigate()

        page.locator('[data-qa-id="email-input"] input').fill("test@email.com")

        page.locator('button[type="submit"]').click()

        page.locator("text=Forgot password?").click()

        assert "reset-password" in page.url

        browser.close()


def test_hudl_login_page():
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")

    email = os.getenv("HUDL_EMAIL")
    password = os.getenv("HUDL_PASSWORD")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)

        login_page.navigate()

        login_page.login(email, password)

        page.locator("text=library").wait_for()
        assert login_page.is_library_visible()

        browser.close()


def test_logout():

    load_dotenv(Path(__file__).resolve().parent.parent / ".env")

    email = os.getenv("HUDL_EMAIL")
    password = os.getenv("HUDL_PASSWORD")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        login_page = LoginPage(page)

        login_page.navigate()

        login_page.login(email, password)

        page.locator("text=MH").first.click()

        page.wait_for_timeout(2000)

        page.get_by_text("Log Out").first.click()

        assert "https://www.hudl.com/" in page.url

        browser.close()
