from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from pathlib import Path
import os
from pages.login_page import LoginPage


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

def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login("invalid@email.com", "invalid1234")

        assert login_page.is_error_message_visible()
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