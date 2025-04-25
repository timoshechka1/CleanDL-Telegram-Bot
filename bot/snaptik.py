from playwright.async_api import async_playwright

async def get_tiktok_download_link(url: str) -> str:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://snaptik.app/en")

        input_selector = "input[name='url']"
        await page.fill(input_selector, url)
        await page.click("button[type='submit']")

        await page.wait_for_selector("a.download-link", timeout=15000)

        element = await page.query_selector("a.download-link")
        download_link = await element.get_attribute("href")

        await browser.close()
        return download_link
