import sys, os, time, re
from playwright.sync_api import Playwright, sync_playwright, expect
from settings import ACCOUNT, PASSWORD, logger

URL_TO_SCRAPE = ''

class ScraperBase():
    def __init__(self, playwright):
        self.playwright = playwright
        self.is_headless = False
        self.browser = None
        self.context = None
        self.page = None
        self.is_authenticated = False
        self.data = None

        self.clear_data()

    def headless(is_headless: bool):
        self.is_headless = is_headless

    def set_data(self, data):
        self.data = data

    def clear_data(self):
        self.set_data({})

    def fetch_data(self):
        return self.data

    def visit(self):
        self.browser = self.playwright.chromium.launch(headless=self.is_headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto(URL_TO_SCRAPE)

    def auth_login(self):
        self.page.get_by_label("E-mail").click()
        self.page.get_by_label("E-mail").fill(ACCOUNT)
        self.page.get_by_label("Password").click()
        self.page.get_by_label("Password").fill(PASSWORD)
        self.page.get_by_role("button", name="Login").click()

        self.is_authenticated = True

    def scrape(self):
        if (self.is_authenticated):
            pass
        else:
            logger.error("Failed not yet authenticated")
            return

        self.set_data({})

    def close(self):
        self.context.close()
        self.browser.close()
