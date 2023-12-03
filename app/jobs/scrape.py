import json
from settings import logger
from playwright.sync_api import Playwright, sync_playwright
from app.scrapers.scrape_base import ScraperBase

def run(playwright: Playwright, imo_no: str) -> None:

    scraper = ScraperBase(playwright)

    scraper.visit()
    scraper.auth_login()

    logger.info("Success login to Equasis Home")
    logger.info("Search information of IMO Number=%s" % imo_no)

    scraper.scrape()

    scraper.close()

    return scraper.fetch_data()
