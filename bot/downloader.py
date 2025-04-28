from playwright.async_api import async_playwright

async def get_tiktok_download_link(tiktok_url: str) -> str:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://snaptik.app/ru")

        await page.fill("input[name='url']", tiktok_url)

        try:
            await page.click("div.modal.is-active div.modal-background", timeout=3000)
        except:
            pass

        await page.click("button[type='submit']")

        await page.wait_for_selector(".download a", timeout=15000)

        download_link = await page.get_attribute(".download a", "href")

        await browser.close()
        return download_link


