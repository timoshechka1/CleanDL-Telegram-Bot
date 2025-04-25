from playwright.async_api import async_playwright

async def get_tiktok_download_link(url: str) -> str:
    async with async_playwright() as p:
        print("Запускаю браузер")
        browser = await p.chromium.launch(headless=False)  # временно headless=False
        page = await browser.new_page()
        print("Перехожу на сайт Snaptik")
        await page.goto("https://snaptik.app/en")

        print("Ввожу ссылку")
        await page.fill("input[name='url']", url)
        await page.click("button[type='submit']")
        print("Ожидаю ссылку на скачивание")

        await page.wait_for_selector("a.download-link", timeout=15000)
        print("Селектор найден")

        element = await page.query_selector("a.download-link")
        download_link = await element.get_attribute("href")
        print("Ссылка на скачивание:", download_link)

        await browser.close()
        return download_link

