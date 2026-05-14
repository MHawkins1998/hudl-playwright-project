from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from pathlib import Path
import os


def test_hudl_login_page():
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
    
    email = os.getenv("HUDL_EMAIL")
    password = os.getenv("HUDL_PASSWORD")


    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.hudl.com/login")
        
        page.locator('[data-qa-id="email-input"] input').fill(email)
        page.locator('button[type="submit"]').click()
        
        page.locator('[data-qa-id="password-input"] input').fill(password)
        page.locator('button[type="submit"]').click()

        page.locator("text=library").wait_for()
        assert page.locator("text=Library").is_visible()