import sys
import settings
import app.jobs.scrape as scrape

if __name__ == '__main__':
    (script_name, command) = sys.argv
    if command == 'scrape':
        with scrape.sync_playwright() as playwright:
            scrape.run(playwright)
