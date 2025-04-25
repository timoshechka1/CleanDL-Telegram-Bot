from playwright.sync_api import sync_playwright
import time

def get_tiktok_download_link(url: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://snaptik.app/en")

        input_selector = "input[name='url']"
        page.fill(input_selector, url)

        page.click("button[type='submit']")

        page.wait_for_selector("a.download-link", timeout=15000)

        download_link = page.query_selector("a.download-link").get_attribute("href")

        browser.close()
        return download_link
